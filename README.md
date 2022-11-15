# Gattungen_und_Emotionen_dhd2023

## Prerequisites

Install requirement.txt (python>=3.6) <br>
Create a folder "models" <br>
Download models and put in models folder <br>
Transform your data to the following input format: <br>

| text        | metadata1           | metadata2  |
| ------------- |:-------------:| -----:|
| first text      | ... | ... |
| second text      | ...      |   ... |
| third text | ...      |    ... |

You can use as many metadata columns as you might need as long
as the "text" column is in your table. The table has to be 
tab-separated.

## Run the model

Change the agrument "-inputfile" in start_prediction.sh.
Run start_prediction.sh. Each emotion prediction will be saved in
a separate output table.
