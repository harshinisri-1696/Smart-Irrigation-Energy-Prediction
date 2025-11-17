
from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Load dataset
df = pd.read_csv("C:/Users/harsh/OneDrive/Desktop/INTERSHIP1/Final/dataset.csv")

# USE ONLY FIRST 100 ROWS
df = df.head(100)

# Train simple prediction model
model = LinearRegression()

# Remove empty energy values
train_df = df.dropna(subset=["Energy_Consumption"])

model.fit(
    train_df[["Temperature", "Humidity", "SoilMoisture"]],
    train_df["Energy_Consumption"]
)

@app.route("/")
def home():
    return render_template("index.html")

# For dashboard averages
@app.route("/get-averages")
def get_averages():
    avg_temp = round(df["Temperature"].mean(), 2)
    avg_hum = round(df["Humidity"].mean(), 2)
    avg_energy = round(df["Energy_Consumption"].mean(), 2)

    return jsonify({
        "avgTemp": avg_temp,
        "avgHum": avg_hum,
        "avgEnergy": avg_energy
    })

# For charts
@app.route("/get-data")
def get_data():
    return jsonify({
        "temperature": df["Temperature"].fillna(0).tolist(),
        "humidity": df["Humidity"].fillna(0).tolist(),
        "soil_moisture": df["SoilMoisture"].fillna(0).tolist(),
        "energy": df["Energy_Consumption"].fillna(0).tolist()
    })

# For prediction
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    temp = float(data["temperature"])
    hum = float(data["humidity"])
    soil = float(data["soil"])

    prediction = model.predict([[temp, hum, soil]])[0]

    return jsonify({"predicted": round(prediction, 2)})

if __name__ == "__main__":
    app.run(debug=True)
