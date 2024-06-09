import pandas as pd
from flask import Flask, request, jsonify
import sqlite3
from sqlalchemy import create_engine
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error
import pickle


df = pd.read_csv(r"data.csv")

df = df.drop(["Location",
            "Education_Level",
            "Occupation",
            "Marital_Status",
            "Employment_Status",
            "Homeownership_Status",
            "Type_of_Housing",
            "Gender",
            "Primary_Mode_of_Transportation"],
             axis=1)

rfr = pickle.load("modelo.sav ")


churro = """sqlite:///dbname.db"""
engine = create_engine(churro)


df.to_sql("df",con=engine, if_exists="replace", index=None)

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/predict', methods=['POST'])
def predict():
     json_ = request.json
     query_df = pd.DataFrame(json_)
     query = pd.get_dummies(query_df)
     prediction = rfr.predict(query)
     return jsonify({'prediction': list(prediction)})
