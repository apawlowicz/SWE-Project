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
    if data[column].dtype == type(object):
        le = LabelEncoder()
        data[column] = le.fit_transform(data[column].tolist())

output_file = open("output_correlation.txt","w")
correlations = data.corr()
print("Correlation matrix", file=output_file)
print(correlations.to_string(), file=output_file)

'''Prints all pairs of features with correlations above a given threshold.'''
print(np.where(correlations.values >= threshold))

data.corr().to_csv('correlations.csv')

corr = data.corr()
ax = sns.heatmap(
    corr, 
    vmin=-1, vmax=1, center=0,
    cmap=sns.diverging_palette(20, 220, n=200),
    square=True
)
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=45,
    horizontalalignment='right'
);

plt.show()
