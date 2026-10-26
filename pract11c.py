from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_openml
from sklearn.linear_model import SGDClassifier

mnist = fetch_openml('mnist_784',version=1,as_frame=False)
x=mnist.data
y = mnist.target.astype(int)
y = (y==5)

x_train,x_test,y_train,y_test = train_test_split(
    x,y,test_size = 0.3,random_state = 1
    )
model = SGDClassifier(random_state = 1)
model.fit(x_train,y_train)

print("training accuracy:",model.score(x_train,y_train)*100)
print("testing accuracy:",model.score(x_test,y_test)*100)
prediction= model.predict([x_test[0]])
if prediction[0]:
    print("digit is 5")
else:
    print("digit is not 5")
