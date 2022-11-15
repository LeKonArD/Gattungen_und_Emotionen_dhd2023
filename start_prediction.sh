#!/bin/sh

python3 predict_shaver.py -modelname "Sadness.pt" 
python3 predict_shaver.py -modelname "Love.pt" 
python3 predict_shaver.py -modelname "Freude.pt" 
python3 predict_shaver.py -modelname "Fear.pt" 
python3 predict_shaver.py -modelname "Anger.pt" 
python3 predict_shaver.py -modelname "Agitation.pt"

