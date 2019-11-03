from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
from prettytable import PrettyTable
import sys, argparse

'''Reads command line arguments, determines number of examples to display and k from it.
Also checks for exceptions.'''

parser = argparse.ArgumentParser(description="K-means clustering, should work in the general case")
parser.add_argument("--k", required=False, default=15, type=int, help="Number of clusters")
parser.add_argument("--examples", required=False, default=5, type=int, help="Number of examples to display per cluster")

args = parser.parse_args()
true_k = args.k
num_examples = args.examples

original_data = pd.read_csv('claims_data.csv', encoding="ISO-8859-1")
data = pd.read_csv('claims_data.csv', encoding="ISO-8859-1")

for column in data.columns:
    if data[column].dtype == type(object):
        le = LabelEncoder()
        data[column] = le.fit_transform(data[column].tolist())

X = data.values.tolist()

model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)

'''Gets the mean values for each column in each cluster.
This can be useful for determining the differences in each cluster.
This is stored in the outputs array.'''
outputs = []
clusters = []
for i in range(true_k):
    cluster = np.take(data.values,np.where(model.labels_ == i),axis=0).squeeze()
    clusters.append(cluster)
    outputs.append([])
    for k in range(data.shape[1]): #k is columns here, don't be confused
        outputs[i].append(np.mean(cluster[:,k]))


table = PrettyTable(data.columns.values.tolist())
for k in range(true_k):
    table.add_row(outputs[k])

output_file = open("output.txt","w")
print(table, file=output_file)

for k in range(true_k):
    table_example = PrettyTable(data.columns.values.tolist())
    print("Cluster " + str(k), file=output_file)
    for i in range(0,num_examples):
        item = clusters[k][i]
        location = -1
        for idx,element in enumerate(X):
            if(element == item.tolist()):
                location = idx
        #location = np.where(np.array(X) == np.array(item), np.array(X), np.array(item)) #should only be one, but what if it's multiple?
        table_example.add_row(original_data.values.tolist()[location])
    print(table_example, file=output_file)