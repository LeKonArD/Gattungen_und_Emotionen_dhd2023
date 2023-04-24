#!/bin/sh

python3 predict_shaver.py -inputfile "example_input.tsv" -modelfile "models/Sadness.pt" 
python3 predict_shaver.py -inputfile "example_input.tsv" -modelfile "models/Love.pt" 
python3 predict_shaver.py -inputfile "example_input.tsv" -modelfile "models/Freude.pt" 
python3 predict_shaver.py -inputfile "example_input.tsv" -modelfile "models/Fear.pt" 
python3 predict_shaver.py -inputfile "example_input.tsv" -modelfile "models/Anger.pt" 
python3 predict_shaver.py -inputfile "example_input.tsv" -modelfile "models/Agitation.pt"

