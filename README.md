# Steps to create a dictionary
1) Export raw data into the `raw_data` repository. Divide into the respective folders.
2) Process the raw data as necessary. The expected output from this processing is a csv of one column of words with no header.
3) Concatenate all word files into one file to be processed.
4) Pass the file to the `create_dictionary.py` script, which will create a list of words sorted by usage. The output is a csv `dictionary.csv` with the columns `word,sequence`.