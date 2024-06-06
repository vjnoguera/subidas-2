from datos_dummy import books
import pandas as pd
from flask import Flask, request
import sqlite3
from sqlalchemy import create_engine
import numpy as np

churro = """sqlite:///dbname.db"""
engine = create_engine(churro)

df = pd.DataFrame(books)
df.to_sql("datos",con=engine, if_exists="replace")

app = Flask(__name__)
app.config["DEBUG"] = True

#esta función es otro endpoint
@app.route("/get_title", methods=["GET"]) # aquí especificacmos el endpoint y el tipo de llamada. la llamada se especifica con una lista o tupla
def title(): # parte importante 2
    filtro = request.args.get("filtro",None)# el get nos permite trabajar sin saber si la key va a estar o no
    if filtro:
        query = f"""SELECT * FROM datos WHERE title = {filtro} LIMIT 1000"""
    else:
        query = f""" SELECT * FROM datos LIMIT 1000"""
    results = pd.read_sql(query, con=engine)

    return results.to_html()

@app.route("/get_id", methods=["GET"]) # aquí especificacmos el endpoint y el tipo de llamada. la llamada se especifica con una lista o tupla
def id(): # parte importante 2
    filtro = request.args.get("filtro",None)# el get nos permite trabajar sin saber si la key va a estar o no
    if filtro:
        query = f"""SELECT * FROM datos WHERE id = {filtro} LIMIT 1000"""
    else:
        query = f""" SELECT * FROM datos LIMIT 1000"""
    results = pd.read_sql(query, con=engine)

    return results.to_html()

    
@app.route("/", methods=["GET"]) # aquí especificacmos el endpoint y el tipo de llamada. la llamada se especifica con una lista o tupla
def WELCOME(): # parte importante 2
    return "WELCOME"

@app.route("/hola", methods=["GET"]) # aquí especificacmos el endpoint y el tipo de llamada. la llamada se especifica con una lista o tupla
def connect(): # parte importante 2
    return """<h1 style ="color:red">Todo OK<h1/>"""

app.run()
