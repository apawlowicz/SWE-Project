import pandas as pd
import sys, argparse
from sklearn.preprocessing import LabelEncoder, scale

#By William Fraher

parser = argparse.ArgumentParser(description="Generates a correlation matrix for a given file.")
parser.add_argument("--file", required=True, default="claims_data.csv", help="File upon which to perform analysis")

args = parser.parse_args()
file = args.file

data = pd.read_csv(file, encoding="ISO-8859-1")

for column in data.columns:
    if data[column].dtype == type(object):
        le = LabelEncoder()
        data[column] = le.fit_transform(data[column].tolist())

output_file = open("output_correlation.txt","w")
print("Correlation matrix", file=output_file)
print(data.corr().to_string(), file=output_file)
