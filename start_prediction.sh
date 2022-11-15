#!/bin/sh

python3 predict_shaver.py -inputfile "example.tsv" -modelname "Sadness.pt" 
python3 predict_shaver.py -inputfile "example.tsv" -modelname "Love.pt" 
python3 predict_shaver.py -inputfile "example.tsv" -modelname "Freude.pt" 
python3 predict_shaver.py -inputfile "example.tsv" -modelname "Fear.pt" 
python3 predict_shaver.py -inputfile "example.tsv" -modelname "Anger.pt" 
python3 predict_shaver.py -inputfile "example.tsv" -modelname "Agitation.pt"

