"""
Script for combining dataframes for each condition.

Usage:
    combine_dataframe.py --filepath=<f>

Options:
    --filepath=<f>      Specify the filepath of all the csv files you want to combine and save the combined csv in.
"""
from docopt import docopt
import os
import pandas as pd
from config import condition_90L_10NL, condition_50L_50NL, condition_10L_90NL

if __name__ == "__main__":
    args = docopt(__doc__)
    filepath = args["--filepath"]
    all_files = [filepath + "/" + item for item in os.listdir(filepath)]
    df = pd.concat(map(pd.read_csv, all_files), ignore_index=True)
    df.to_csv(filepath + "/combine.csv", index=False)
