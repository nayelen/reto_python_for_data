import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def linea_temporal(df,x,y):
  plt.figure(figsize=(10,3))
  sns.lineplot(data=df,x=x,y=y, color='purple', marker='o')
  plt.xlabel('Fecha pedidos')
  plt.ylabel('Número de pedidos')
  plt.xticks(rotation=45)
  plt.title('Línea temporal de pedidos por fecha');
  
def barras(df):
  plt.figure(figsize=(10,4))
  plt.bar(df.index, df.values, color= 'blue')
  plt.title('Ventas por Continente', fontsize=14)
  plt.xlabel('Continente')
  plt.ylabel('Cantidad de Pedidos');
  
  
def barplot(df, x, y,palette):
  plt.figure(figsize=(12,6))
  sns.barplot(data=df, x=x, y=y, palette=palette, hue=y)
  plt.xlabel(f'{x}')
  plt.ylabel(f'{y}')
  plt.title(f'Barplot {x} for {y}');
  
def barh( x, y,color):
  plt.figure(figsize=(12,6))
  plt.barh(x,y, color=color)
  plt.xlabel("Cantidad Vendida")
  plt.ylabel("Producto")
  plt.title("Top 10 Productos Más Vendidos")
  plt.gca().invert_yaxis()  # Invierte el eje Y para que el más vendido esté arriba
  plt.show()
  
