from flask import Flask, render_template, request
from database.db import *

app = Flask(__name__)

@app.route('/register_page')
def register_page():
    return render_template("RegisterCris.html")

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
    if result == "Duplicate ID":
        return "Error: Duplicate ID"
    elif result == "Error":
        return "An error occurred while adding the motorcycle"
    return "Motorcycle Added"

     
if __name__ == "__main__":    
    host = "172.31.35.175"
    port = 80
    app.run(host, port, True)