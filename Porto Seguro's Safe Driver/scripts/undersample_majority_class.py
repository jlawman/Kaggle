from imblearn.under_sampling import RandomUnderSampler

rus = RandomUnderSampler(random_state=0)
train_undersampled, train_target_undersampled = rus.fit_sample(train, train_target)

print('New target value counts: {}'.format(np.bincount(train_target_undersampled)))