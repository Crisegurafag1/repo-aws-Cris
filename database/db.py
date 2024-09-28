import pymysql

host = "database-cris.cxu6a68uodj1.us-east-2.rds.amazonaws.com"
user = "cristian"
passw = "Solucion24+"
db_name="dbConcesionario"

def connection_SQL():
    try:
        conecction = pymysql.connect(
            host=host,
            user=user,
            password=passw,
            database=db_name
        )
        print("Succesfull connection to database")
        return conecction
    except Exception as err:
        print("Error", err)
        return None
    
def insert(id, marca, modelo, cilindraje, color, precio):
    try:
        instruction = "INSERT INTO tbMotocicletas (id, marca, modelo, cilindraje, color, precio) VALUES (%s, %s, %s, %s, %s, %s)"
        connection = connection_SQL()
        cursor = connection.cursor()
        cursor.execute(instruction, (id, marca, modelo, cilindraje, color, precio))
        connection.commit()
        print("Motocicleta Agregada")
    except pymysql.err.IntegrityError as err:
        print("Error: Duplicate ID", err)
        return "Duplicate ID"
    except Exception as err:
        print("Error", err)
        return None
    finally:
        cursor.close()
        connection.close()

def consult(id):
    try:
        instruction = "SELECT * FROM dbConcesionario.tbMotocicletas WHERE id=" + id
        connection = connection_SQL()
        cursor = connection.cursor()
        cursor.execute(instruction)
        result = cursor.fetchall()
        return result          
    except Exception as err:
        print("Error", err)
        return None