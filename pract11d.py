from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold,cross_val_score

data = load_iris()
x=data.data
y = data.target



model = LogisticRegression(max_iter = 1000)
kfold = KFold(n_splits= 5,shuffle=True,random_state=1)
scores = cross_val_score(model,x,y,cv=kfold)

print("cross validation score:",scores)
print("average accuracy:",format(scores.mean()*100))

