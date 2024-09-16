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
        
def insert():
    instruction = "INSERT INTO tbMotocicletas (marca, modelo, cilindraje, color, precio) VALUES('Yamaha', 'YZF-R3', '321cc', 'Azul', 20000000);"
    conecction = connection_SQL()
    cursor = conecction.cursor()
    cursor.execute(instruction)
    conecction.commit()
    print("Motocicleta Agregada")

insert()