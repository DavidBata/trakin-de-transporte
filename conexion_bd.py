import psycopg2
def consulta_transporte():
    try:
        connection=psycopg2.connect(
            database='adempiere',
            host='losroques',
            port='5434',
            user='adempiere',
            password='ad3mp13r3sf1d4',

        )
        print('conexion exitosa')

        cursor= connection.cursor()
        cursor.execute("SELECT version()")
        row=cursor.fetchone()
        print(row)
        cursor.execute('SELECT * FROM status_vehiculo_taller_transporte')  
        rows=cursor.fetchall()
        list=[]
        for row in rows:
            print(row)
            list.append(row)
        connection.close()    
        return list
    
    except Exception as ex:
        print(ex)   
        return ex
    finally:
        print('conexion finalizada')
        
    
