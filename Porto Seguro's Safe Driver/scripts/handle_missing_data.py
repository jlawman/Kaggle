# Replace -1 values (missing values) with nan
train = train.replace(to_replace=-1,value=np.nan)
test = test.replace(to_replace=-1,value=np.nan)

# Missing data 1: drop columns with 20%+ missing data
incomplete_columns = list(train.isnull().sum()[train.isnull().sum()>len(train)*.2].index)

train = train.drop(incomplete_columns,axis=1)
test = test.drop(incomplete_columns, axis=1)

# Missing data 2: impute median values
train = train.fillna(train.median())
test = test.fillna(test.median())