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
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None
    
def insert(id, marca, modelo, cilindraje, color, precio):
    try:
        connection = connection_SQL()
        if connection is None:
            raise Exception("Failed to connect to the database")
        cursor = connection.cursor()
        
        # Verificar si el ID ya existe
        cursor.execute("SELECT id FROM tbMotocicletas WHERE id = %s", (id,))
        if cursor.fetchone():
            raise Exception(f"ID {id} already exists in the database")
        
        query = "INSERT INTO tbMotocicletas (id, marca, modelo, cilindraje, color, precio) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (id, marca, modelo, cilindraje, color, precio))
        connection.commit()
        cursor.close()
        connection.close()
        print("Data inserted successfully")
        return True
    except Exception as e:
        print(f"Error inserting data: {e}")
        return False




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