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
    try:
        data = request.form
        file = request.files
        print(f"Received data: {data}")
        print(f"Received file: {file}")
        id = data["id"]
        marca = data["marca"]
        modelo = data["modelo"]
        cilindraje = data["cilindraje"]
        color = data["color"]
        precio = data["precio"]
        photo = file["photo"]
        
        # Intentar insertar los datos en la base de datos primero
        result = insert(id, marca, modelo, cilindraje, color, precio)
        if result:
            # Si la inserción es exitosa, subir la imagen al bucket de S3
            sesion_s3 = connectionS3()
            photo_path, photo_name = save_file(id, photo)
            upload_file_s3(sesion_s3, photo_path, photo_name)
            return jsonify({"message": "Motorcycle Added Successfully"}), 200
        else:
            return jsonify({"message": "Error adding motorcycle"}), 500
    except Exception as e:
        print(f"Error in register_inventory: {e}")
        return jsonify({"message": f"Error adding motorcycle: {e}"}), 500



@app.route('/consult_inventory', methods=["post"])
def consult_inventory():
    id = request.get_json().get('id')
    print(f"Consulting inventory for ID: {id}")
    result = consult(id)
    print(f"Result from database: {result}")
    if result:
        sesion_s3 = connectionS3()
        bucket_project = sesion_s3.Bucket(bucket_name)
        bucket_objects = bucket_project.objects.filter(Prefix=f"images/{id}.")
        photo_url = None
        for obj in bucket_objects:
            photo_url = f"https://{bucket_name}.s3.amazonaws.com/{obj.key}"
            break
        if not photo_url:
            return jsonify({"error": "Photo not found"}), 404
        resp_data = {  
            'id': result[0][0],     
            'marca': result[0][1],
            'modelo': result[0][2], 
            'cilindraje': result[0][3], 
            'color': result[0][4],
            'precio': result[0][5],
            'photo_url': photo_url
        }
        return jsonify(resp_data)
    else:
        return jsonify({"error": "No data found"}), 404
