import pandas as pd
import numpy as np
import os

os.chdir ("/home/liam/Dropbox/DCU/ML/Assignment/")#change directory to where you downloaded your dataset

#Common to use pandas and numpy to manipulate data in ML
#main workhorse in pandas is a dataframe that's conventionally short-handed to df

df = pd.read_json ("fake_news.json", lines = True)#similar func for reading csv files etc
df = df.drop(columns =['article_link']) #delete a column by name
df["is_sarcastic"] = df["is_sarcastic"].astype("category") #useful if what should be an integer was read-in as a string or similar problem
df = df.drop(df.index[7302]) #Delete a specific row of a dataframe
#df.drop_duplicates(subset = 'headline',keep = False, inplace = True) #code to remove duplicate headlines to repeat analysis

#Check for missing values
nas =df['headline'].isna().sum()#simply counts how many NA values are in this column
nuls = df['headline'].isnull().sum()
print("Number of NA values in dataset: ", nas)
print ("Number of NULL values in dataset: ", nuls)

##Figure 1. Basic value count
pd.value_counts(df['is_sarcastic'])
print(counts) ##note 0 = real news, 1 = fake news
