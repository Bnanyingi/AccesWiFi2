from sklearn.naive_bayes import GaussianNB
clf = GaussianNB() 
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
