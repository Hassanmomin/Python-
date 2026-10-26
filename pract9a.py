import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

df = pd.read_csv("play tennis.csv")
print("original dataset")
print(df)

encoder = LabelEncoder()
for column in df.columns:
    df[column] = encoder.fit_transform(df[column])

x = df[["outlook", "temp", "humidity", "wind"]]
y = df["play tennis"]

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=42)

model = GaussianNB()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

print("\n predicted value:")
print(y_pred)
print("\n Actual value:")
print(y_test.values)

accuracy = accuracy_score(y_test, y_pred)
print("\n Accuracy:", accuracy * 100, "%")
