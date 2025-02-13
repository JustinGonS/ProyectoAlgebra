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
    
    # Paso 1: Mostrar la matriz aumentada inicial
    st.write("Paso 1: Matriz aumentada inicial")
    st.write(matriz_ampliada)
    st.markdown("La matriz aumentada es una combinación de la matriz original y la matriz identidad.")
    
    paso_num = 2  # Iniciamos la numeración de los pasos desde el paso 2 (después de la matriz inicial)
    
    for i in range(n):
        pivote = matriz_ampliada[i, i]
        
        # Si el elemento diagonal es 0, buscamos una fila que lo haga diferente de 0
        if pivote == 0:
            for j in range(i+1, n):
                if matriz_ampliada[j, i] != 0:
                    matriz_ampliada[[i, j]] = matriz_ampliada[[j, i]]  # Intercambiamos las filas
                    break
        
        # Dividimos la fila i por el pivote solo si no es 1
        if pivote != 1:
            matriz_ampliada[i] = matriz_ampliada[i] / pivote
            st.markdown(f"Paso {paso_num}: Hacer el pivote de la fila {i+1}. Dividimos toda la fila {i+1} por el elemento {pivote:.2f} para que el pivote sea 1.")
            st.write(matriz_ampliada)
            paso_num += 1
        else:
            st.markdown(f"Paso {paso_num}: El pivote de la fila {i+1} ya es 1, no es necesario dividir.")
            paso_num += 1
        
        # Restamos múltiplos de la fila i de las otras filas solo si el factor no es 0
        for j in range(n):
            if j != i:
                factor = matriz_ampliada[j, i]
                if factor != 0:  # Solo realizamos la resta si el factor no es 0
                    matriz_ampliada[j] -= factor * matriz_ampliada[i]
                    st.markdown(f"Paso {paso_num}: Restamos {factor:.2f} veces la fila {i+1} de la fila {j+1} para hacer ceros en la columna {i+1}.")
                    st.write(matriz_ampliada)
                    paso_num += 1
    
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
