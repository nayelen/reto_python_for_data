import pandas as pd
import psycopg2
from src import passwords as ps

# def eda_preliminar(df):

#    print(f'El conjunto de datos tiene {df.shape[0]} filas y {df.shape[1]} columnas')
#    print('---------------------------------')
#    print(f'Tenemos un total de {df.duplicated().sum()} valores duplicados')
#    print('---------------------------------')
#    display(df.info())
#    print('---------------------------------')
#    print('Tenemos los siguientes porcentajes nulos: ')
#    display(df.isnull().sum()/df.shape[0]*100)
#    print('---------------------------------')
#    print ('Los estadisticos principales de las columnas numericas son:')
#    display(df.describe().T)
#    print('---------------------------------')
#    print('Los estadisticos principales de las columnas categoricas son:')
#    display(df.describe(include="O").T)
#    print('---------------------------------')
#    for col in df.select_dtypes(include='O').columns:
#       print(f'Para la columna {col.upper()}:')  
#       display(df[col].value_counts())
#       print('---------------------------')
#       print('Estadísticos descriptivos de la columna:')

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