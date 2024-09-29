from flask import Flask, render_template, request, jsonify
from serverCris import app
from database.db import *
from controllers.admin_s3 import *

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
    file = request.files
    id = data["id"]
    marca = data["marca"]
    modelo = data["modelo"]
    cilindraje = data["cilindraje"]
    color = data["color"]
    precio = data["precio"]
    photo = file["photo"]
    sesion_s3 = connectionS3()
    photo_path, photo_name = save_file(id, photo)
    upload_file_s3(sesion_s3 ,photo_path, photo_name)
    result = insert(id, marca, modelo, cilindraje, color, precio)
    return "Motorcycle Added"

@app.route('/consult_inventory', methods=["post"])
def consult_inventory():
    id = request.get_json()
    result = consult(id)
    print(result)
    resp_data = {  
        'id':result[0][0],     
	    'marca':result[0][1],
        'modelo':result[0][2], 
        'cilindraje':result[0][3], 
        'color':result[0][4],
        'precio':result[0][5]
    }
    return jsonify(resp_data)