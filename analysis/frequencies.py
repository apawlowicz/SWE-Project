import pandas as pd
import sys, argparse
from sklearn.preprocessing import LabelEncoder, scale
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#By William Fraher

parser = argparse.ArgumentParser(description="Generates a correlation matrix for a given file.")
parser.add_argument("--file", required=True, default="policy_data.csv", help="File upon which to perform analysis")
parser.add_argument("--threshold", required=False, default=0.1, type=float, help="Minimum value for correlations to be printed.")

args = parser.parse_args()
file = args.file
threshold = args.threshold

print(file)
data = pd.read_csv(file, encoding="ISO-8859-1")

for column in data.columns:
    print(column)
    print(data[column].value_counts())
    print('-----------')
