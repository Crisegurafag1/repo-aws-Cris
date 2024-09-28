from flask import Flask, render_template, request
from serverCris import app
from database.db import *

@app.route('/home_page')
def home_page():
    return render_template("HomeCris.html")

@app.route('/register_page')
def register_page():
    return render_template("RegisterCris.html")

@app.route('/consult_page')
def consult_page():
    return render_template("ConsultCris.html")

@app.route('/register_inventory', methods=["post"])
def register_inventory():
    data = request.form
    id = data["id"]
    marca = data["marca"]
    modelo = data["modelo"]
    cilindraje = data["cilindraje"]
    color = data["color"]
    precio = data["precio"]
    result = insert(id, marca, modelo, cilindraje, color, precio)
    return "Motorcycle Added"

@app.route('/consult_inventory', methods=["post"])
def consult_inventory():
    id = request.get_json()
    result = consult(id)
    print(result)
    return "El usuario ha sido consultado"