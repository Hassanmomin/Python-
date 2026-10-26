from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
x = iris.data
y = iris.target

x_train,x_test,y_train,y_test = train_test_split(
    x,y,test_size=0.3,random_state=1
    )
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train,y_train)
train_pred=knn.predict(x_train)
train_accuracy = accuracy_score(y_train,train_pred)
test_pred = knn.predict(x_test)
test_accuracy = accuracy_score(y_test,test_pred)
print("training accuracy:",train_accuracy)
print("testing accuracy:",test_accuracy)
print(test_pred)
print("\nActual values:")
print(y_test)
