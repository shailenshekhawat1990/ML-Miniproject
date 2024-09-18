import pandas as pd

pd=pd.read_csv(r'C:\Users\HP\Downloads\resources-staging_5265_Machine Learning Mini Project 1 (1)\resources-staging_5265_Machine Learning Mini Project 1 (1)\creditcard.csv')
print(pd)

shape = pd.shape
print("Shape:", shape)
print("Missing Values:")
print("Summary Statistics:")

class_counts = pd['Class'].value_counts()
print("Class Distribution:")
print(class_counts)


