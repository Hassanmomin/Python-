import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

iris = load_iris()
df = pd.DataFrame(iris.data,columns=iris.feature_names)
df['target'] = iris.target

print("first 5 row of dataset:")
print(df.head())

x = df.drop('target',axis = 1)
y = df['target']
scalar = StandardScaler()
x_scaled = scalar.fit_transform(x)

x_train,x_test,y_train,y_test = train_test_split(
    x_scaled,y,test_size = 0.2,random_state = 42
    )

model = LogisticRegression()
model.fit(x_train,y_train)

y_train_pred = model.predict(x_train)
y_test_pred = model.predict(x_test)
train_acc =  accuracy_score(y_train,y_train_pred)
test_acc =  accuracy_score(y_test,y_test_pred)
print("training accuracy:",train_acc)
print("testing accuracy:",test_acc)








