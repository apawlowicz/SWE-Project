import pandas as pd
import sys, argparse
from sklearn.preprocessing import LabelEncoder, scale
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#By William Fraher

def getFrequencies(file):
    print(file)
    
    data = pd.read_csv("uploads/" + file, encoding="ISO-8859-1")

    counts = {}
    for column in data.columns:
        entry = []
        entry.append(data[column].value_counts().tolist()[0:min(len(data[column].value_counts().tolist()),10)])
        entry.append(data[column].value_counts().index.tolist()[0:min(len(data[column].value_counts().index.tolist()),10)])
        counts[column] = entry
    
    return counts
