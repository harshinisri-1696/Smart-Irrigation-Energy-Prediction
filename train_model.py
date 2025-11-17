import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data = pd.read_csv("C:/Users/harsh/OneDrive/Desktop/INTERSHIP1/Final/dataset.csv")

X = data[['Temperature', 'Humidity']]
y = data['Energy_Consumption']

model = LinearRegression()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))

print("Model Trained and Saved!")
