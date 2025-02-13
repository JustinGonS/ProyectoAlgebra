import streamlit as st
import numpy as np

def es_invertible(matriz):
    """Verifica si la matriz es invertible comprobando su determinante"""
    return np.linalg.det(matriz) != 0

def calcular_inversa(matriz):
    """Calcula la inversa de una matriz utilizando Gauss-Jordan"""
    n = matriz.shape[0]
    # Crear una matriz identidad
    identidad = np.eye(n)
    # Realizamos una copia de la matriz original para no modificarla
    matriz_ampliada = np.hstack([matriz, identidad])
    
    # Aplicamos el algoritmo de eliminación de Gauss-Jordan
    for i in range(n):
        # Asegurarnos de que el pivote no sea 0
        if matriz_ampliada[i, i] == 0:
            for j in range(i+1, n):
                if matriz_ampliada[j, i] != 0:
                    # Intercambiamos filas
                    matriz_ampliada[[i, j]] = matriz_ampliada[[j, i]]
                    break
        # Normalizamos el pivote
        matriz_ampliada[i] = matriz_ampliada[i] / matriz_ampliada[i, i]
        
        # Hacemos cero los elementos debajo y encima del pivote
        for j in range(n):
            if j != i:
                matriz_ampliada[j] -= matriz_ampliada[j, i] * matriz_ampliada[i]
        
        # Mostrar el paso actual
        st.write(f"Paso {i+1}:")
        st.write(matriz_ampliada[:, n:])  # Mostrar solo la parte de la inversa
    
    return matriz_ampliada[:, n:]

st.title("Calculadora de Matriz Inversa con Gauss-Jordan")

n = st.number_input("Tamaño de la matriz (n x n):", min_value=2, max_value=10, step=1, value=2)

matriz = []
for i in range(n):
    fila = st.text_input(f"Fila {i+1} separada por espacios:", " ".join(["0"]*n))
    matriz.append(list(map(float, fila.split())))

matriz = np.array(matriz)

if st.button("Calcular Inversa"):
    if es_invertible(matriz):
        inversa = calcular_inversa(matriz)
        st.write("Matriz Inversa:")
        st.write(inversa)
    else:
        st.error("La matriz no es invertible (determinante = 0).")
