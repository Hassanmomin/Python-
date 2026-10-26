from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.tree import DecisionTreeRegressor

data = fetch_california_housing()
x = data.data
y = data.target

x_train,x_test,y_train,y_test = train_test_split(
    x,y,test_size=0.3,random_state=1
    )
model = DecisionTreeRegressor(random_state=1)
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print("Mean squared Error:",mean_squared_error(y_test,y_pred))
print("R2 score:",r2_score(y_test,y_pred))
pridiction = model.predict([x_test[0]])
print("pridiction class:",pridiction[0])
