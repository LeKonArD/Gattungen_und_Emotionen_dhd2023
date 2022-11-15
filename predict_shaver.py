import os
os.environ["CUDA_VISIBLE_DEVICES"]="2"
from transformers import BertTokenizerFast, BertModel, BertConfig, BertForTokenClassification, TextDataset
from transformers import AdamW, PreTrainedTokenizer, PreTrainedTokenizerFast, BertForSequenceClassification,get_cosine_schedule_with_warmup
from transformers import get_linear_schedule_with_warmup, Trainer, DataCollatorForTokenClassification, AdamWeightDecay
import numpy as np
from torch.utils.data import DataLoader, RandomSampler, TensorDataset, SequentialSampler
import torch
from tqdm.notebook import tqdm
import os
import pandas as pd
from sklearn.utils import shuffle
from sklearn.metrics import f1_score, accuracy_score
import json
from collections import Counter
from sklearn.metrics import classification_report
from tqdm.notebook import tqdm
import argparse
from dataclasses import dataclass, field
from typing import Optional
import torch.nn as nn
from sklearn.model_selection import  train_test_split
import random
import re
import argparse
from scipy.stats import pearsonr
from sklearn.metrics import mean_squared_error
import pickle as pkl
from tqdm import tqdm

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-modelname', type=str)
args = parser.parse_args()
modelname = args.modelname


def load_checkpoint_cls(model_name, path):
    
    model = BertForSequenceClassification.from_pretrained(model_name)
    state_dict = torch.load(path)

    mkeys = list(model.state_dict().keys())
    skeys = list(state_dict.keys())


    for k in skeys:

        if k not in mkeys:
            del state_dict[k]

    mkeys = list(model.state_dict().keys())
    skeys = list(state_dict.keys())

    for k in mkeys:

        if k not in skeys:
            state_dict[k] = model.state_dict()[k]


    model.load_state_dict(state_dict)
    
    
    return model

model = load_checkpoint_cls("deepset/gbert-large","models/"+modelname)
tokenizer = BertTokenizerFast.from_pretrained("deepset/gbert-large", padding_side="left", padding="max_length")

data = pd.read_csv("enc_input.tsv", sep="\t", index_col=0)

def deploy_tokenizer(T):
    
    tokenizer_output = tokenizer.encode_plus(T, padding="max_length", truncation=True)
    
    inputs = np.array(tokenizer_output["input_ids"])
    attention_mask = np.array(tokenizer_output["input_ids"])
    
    if len(inputs) != 512:
        print(len(inputs))
    
    return inputs, attention_mask

def clean(x):
    
    x = re.sub("\n|\[|\]","",x)
    x = re.sub("\s+"," ",x)
    x = x.split(" ")[1:]
    x = [int(y) for y in x]
    return x

model.cuda()

result = []
for index, row in tqdm(data.iterrows(),total=len(data)):
    #x = clean(row["text"])
    x, a = deploy_tokenizer(row["text"])
    output = model(torch.tensor(np.stack([x,x])).to("cuda"))
    label = np.argmax(output["logits"][0].detach().cpu().numpy())
    result.append(label)
    
    
    
data[modelname] = result
data.to_csv(modelname+"_prediction.tsv", sep="\t")
