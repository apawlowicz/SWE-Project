import pandas as pd
import sys, argparse
from sklearn.preprocessing import LabelEncoder, scale
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from prettytable import PrettyTable
import itertools

#By William Fraher

parser = argparse.ArgumentParser(description="Generates a correlation matrix for a given file.")
parser.add_argument("--file", required=True, default="policy_data.csv", help="File upon which to perform analysis")
parser.add_argument("--threshold", required=False, default=0.1, type=float, help="Minimum value for correlations to be printed.")
parser.add_argument("--maximum", required=False, default=10, type=int, help="Number of elements to display per category.")

args = parser.parse_args()
file = args.file
threshold = args.threshold
maximum = args.maximum
data = pd.read_csv(file, encoding="ISO-8859-1")

output_file = open("frequencies.txt","w",encoding="ISO-8859-1")
for column in data.columns:
    print(column, file=output_file)
    print(data[column].value_counts().index.tolist()[0:maximum], file=output_file)
    print(data[column].value_counts().tolist()[0:maximum], file=output_file)
    print("\n", file=output_file)
