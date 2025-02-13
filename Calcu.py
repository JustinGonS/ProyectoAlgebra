import streamlit as st
import numpy as np

def es_invertible(matriz):
    """Verifica si la matriz es invertible comprobando su determinante"""
    return np.linalg.det(matriz) != 0

def calcular_inversa(matriz):
    """Calcula la inversa de una matriz"""
    return np.linalg.inv(matriz)

st.title("Calculadora de Matriz Inversa")

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
