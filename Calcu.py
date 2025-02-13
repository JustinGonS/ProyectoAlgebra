import streamlit as st
import numpy as np

def es_invertible(matriz):
    """Verifica si la matriz es invertible comprobando su determinante"""
    return np.linalg.det(matriz) != 0

def calcular_inversa(matriz):
    """Calcula la inversa de una matriz utilizando Gauss-Jordan"""
    n = matriz.shape[0]
    identidad = np.eye(n)
    matriz_ampliada = np.hstack([matriz, identidad])
    
    for i in range(n):
        if matriz_ampliada[i, i] == 0:
            for j in range(i+1, n):
                if matriz_ampliada[j, i] != 0:
                    matriz_ampliada[[i, j]] = matriz_ampliada[[j, i]]
                    break
        matriz_ampliada[i] = matriz_ampliada[i] / matriz_ampliada[i, i]
        for j in range(n):
            if j != i:
                matriz_ampliada[j] -= matriz_ampliada[j, i] * matriz_ampliada[i]
        
        st.write(f"Paso {i+1}:")
        st.write(matriz_ampliada[:, n:])
    
    return matriz_ampliada[:, n:]

# Teoría
st.title("Calculadora de Matriz Inversa con Gauss-Jordan")
st.markdown("""
### Teoría: Método de Gauss-Jordan

El **método de Gauss-Jordan** es una técnica de álgebra lineal utilizada para encontrar la **inversa de una matriz**. La idea es aplicar operaciones elementales sobre las filas de una matriz para convertir la parte izquierda en la **matriz identidad** mientras modificamos la parte derecha para obtener la matriz inversa.

#### Pasos:
1. Combina la matriz original con la matriz identidad.
2. Realiza operaciones elementales en las filas para transformar la matriz original en la identidad.
3. La parte derecha será la inversa de la matriz original.

#### Ejemplo:
Supongamos que tenemos la siguiente matriz 2x2:

""")

# Usamos st.latex() para las ecuaciones matemáticas
st.latex(r'''
A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}
''')

st.markdown("""
La matriz identidad de 2x2 es:

""")

st.latex(r'''
I = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}
''')

st.markdown("""
Combinamos la matriz \(A\) y \(I\) para formar la matriz aumentada:

""")

st.latex(r'''
[A | I] = \begin{bmatrix} 1 & 2 & | & 1 & 0 \\ 3 & 4 & | & 0 & 1 \end{bmatrix}
''')

st.markdown("""
A partir de aquí, aplicamos las operaciones de Gauss-Jordan para obtener la inversa de la matriz \(A\).
""")

# Interacción del usuario para ingresar la matriz
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
