import pandas as pd
import psycopg2
from src import passwords as ps

conn = psycopg2.connect(host= 'localhost',
                        database = "Northwind",
                        user= "postgres",
                        password = ps.pass_psycopg)
cursor = conn.cursor()
cursor.execute("SELECT version();")
cursor.fetchone()

def pasos_querys(args):
  #creo una funcion reutilizable
  conn.rollback() 
  cursor.execute(args)  # Ejecutamos la query
  filas= cursor.fetchall() # creo variable con el resultado de la query para las filas
  nombres_col = [elemento[0] for elemento in cursor.description ] # Recuperamos los nombres de las columnas de la BBDD
  df_result = pd.DataFrame(data=filas, 
                           columns = nombres_col)
  return df_result

