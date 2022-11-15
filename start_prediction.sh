#!/bin/sh

python3 predict_shaver.py -modelname "MLG_500_Sadness_0.74.pt" 
python3 predict_shaver.py -modelname "MLG_500_Love_0.77.pt" 
python3 predict_shaver.py -modelname "MLG_500_Freude_0.73.pt" 
python3 predict_shaver.py -modelname "MLG_500_Fear_0.79.pt" 
python3 predict_shaver.py -modelname "MLG_500_Anger_0.71.pt" 
python3 predict_shaver.py -modelname "MLG_500_Agitation_0.62.pt"

