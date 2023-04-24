# Gattungen_und_Emotionen_dhd2023

## Prerequisites

Install requirement.txt (python>=3.6) <br>
Create a folder "models" <br>
[Download](https://owncloud.gwdg.de/index.php/s/g2PjWWcknSRlMSd) the models to your "models" folder <br>
Transform your data to the following input format: <br>

documents | text          | metadata1           | metadata2  |
----------| ------------- |:-------------:| -----:|
d1        | first line    | ... | ... |
d1        | second line   | ... | ... |
d2        | first line    | ... | ... |

You can use as many metadata columns as you might need as long
as the "text" column is in your table. The table has to be 
tab-separated.

## Run the model

Change the agrument "-inputfile" in start_prediction.sh.
Run start_prediction.sh. Each emotion prediction will be saved in
a separate output table.
