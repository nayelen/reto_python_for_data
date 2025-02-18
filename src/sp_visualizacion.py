import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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
  
def boxplot(df, x, y):
  plt.figure(figsize=(10,3))
  sns.boxplot(data=df , x=x, y=y)
  plt.ylabel('Fecha envio')
  plt.xlabel('Compañía de transporte')
  plt.title('Boxplot de fecha de envío');
  
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
  

def plot_barh_dual(x, y1, y2, label1="Stock Disponible", label2="Cantidad Vendida", color1='red', color2='gray', alpha2=0.6, title="Stock Crítico vs. Demanda", xlabel="Unidades", ylabel="Producto"):
    plt.figure(figsize=(12,6))
    
    # Primera barra (Stock Disponible)
    plt.barh(x, y1, color=color1, label=label1)
    
    # Segunda barra (Cantidad Vendida) apilada sobre la primera
    plt.barh(x, y2, left=y1, color=color2, alpha=alpha2, label=label2)
    
    # Etiquetas y título
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    
    # Asegurar que las etiquetas de productos sean visibles
    plt.yticks(x, x)
    
    # Mostrar leyenda
    plt.legend()
    
    plt.show()
