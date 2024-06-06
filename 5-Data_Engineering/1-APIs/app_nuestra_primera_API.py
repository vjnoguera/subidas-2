from flask import Flask, request
import sqlite3
from sqlalchemy import create_engine
import pandas as pd


churro = """sqlite:///dbname.db"""
engine = create_engine(churro)

df = pd.DataFrame({"col1":[1,2,3,4,5], "col2":list("abcde")})
df.to_sql("datos",con=engine, if_exists="replace")

# esto inicializa la app
app = Flask(__name__) # parte importante 1

#esta función es el endpoint
@app.route("/hola", methods=["GET"]) # aquí especificacmos el endpoint y el tipo de llamada. la llamada se especifica con una lista o tupla
def connect(): # parte importante 2
    return """ <h1 style ="color:red">Todo OK<h1/>"""

#esta función es otro endpoint
@app.route("/", methods=["GET"]) # aquí especificacmos el endpoint y el tipo de llamada. la llamada se especifica con una lista o tupla
def WELCOME(): # parte importante 2
    return "WELCOME"

#esta función es otro endpoint
@app.route("/get_data", methods=["GET"]) # aquí especificacmos el endpoint y el tipo de llamada. la llamada se especifica con una lista o tupla
def data(): # parte importante 2
    filtro = request.args.get("filtro",None)# el get nos permite trabajar sin saber si la key va a estar o no
    if filtro:
        query = f"""SELECT * FROM datos WHERE col2 = {filtro} LIMIT 1000"""
    else:
        query = f""" SELECT * FROM datos LIMIT 1000"""
    results = pd.read_sql(query, con=engine)

    return results.to_html()


# esto ejecuta la app
app.run(debug=True) # parte importante 3

