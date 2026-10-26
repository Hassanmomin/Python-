from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
from sklearn.metrics import mean_squared_error,r2_score

x,y = make_regression(
    n_samples = 100,
    n_features = 1,
    noise = 10,
    random_state = 42
    )

x_train,x_test,y_train,y_test = train_test_split(
    x,y,test_size = 0.2,random_state = 42
    )
model=LinearRegression()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
msc = mean_squared_error(y_test,y_pred)
r2 = r2_score(y_test,y_pred)
print("model coefficient:",model.coef_)
print("model intercept:",model.intercept_)
print("mean square error:",msc)
print("r2 score:",r2)
