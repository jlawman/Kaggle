from imblearn.over_sampling import SMOTE

smote = SMOTE(ratio='minority')
train_resampled, train_target_resampled = smnote.fit_sample(train, train_target)

print('New target value counts: {}'.format(np.bincount(train_target_resampled)))