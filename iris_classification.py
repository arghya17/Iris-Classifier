from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import neighbors, metrics
iris=datasets.load_iris()
x=iris.data
y=iris.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.5)
classifier=neighbors.KNeighborsClassifier(n_neighbors=5)
classifier.fit(x_train,y_train)
predictions=classifier.predict(x_test)
print(metrics.accuracy_score(y_test,predictions))
