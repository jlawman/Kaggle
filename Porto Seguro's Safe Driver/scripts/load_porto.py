import pandas as pd
import numpy as np

#Import data
train = pd.read_csv('../data/train.csv')
test = pd.read_csv('../data/test.csv')

#Create train and test variables
train_id = train['id']
train_target = train['target']
train = train.drop(['id','target'],axis=1)

test_id = test['id']
test = test.drop('id',axis=1)