#EJERCICIOS PARA EL IDL3
import streamlit as st
import numpy as np
st.title("EJERCICIOS PROPUESTOS PARA EL CASO PROPUESTO IDL 3")
#Ejercicio..6 

st.subheader("Ejercicio 6: Array de Números ingresados por usuario y determinar cual es el mayor")

# Entrada para el tamaño del array
tamaño_array = st.number_input("Ingresa el tamaño del array:", min_value=1, value=5, step=1)

# Ingreso de valores del array
array_numeros = []
for i in range(int(tamaño_array)):
    numero = st.number_input(f"Ingrese el número para la posición {i + 1}:", min_value=0)
    array_numeros.append(numero)

# Convertimos la lista a un array de numpy
array_numeros = np.array(array_numeros)

# Encontrar el valor máximo en el array
valor_maximo = np.max(array_numeros)

# Mostrar resultados
st.write("Array ingresado:", array_numeros)
st.write(f"El mayor de todos los valores es: {valor_maximo}")

# Ejercicio..1

st.subheader("Ejercicio 1: Calculadora con las cuatro operaciones")
numero1 = st.number_input("Ingrese primer número a operar", min_value = 1)
numero2 = st.number_input("Ingrese segundo número a operar", min_value = 1)
st.write("Selecciona una de las 4 operaciones")
menus = ["Multiplicar","Dividir","Sumar","Restar"]
seleccion = ""
seleccion = st.radio("4 operaciones", menus)

def cuatro_operaciones():
    if seleccion == "Multiplicar":
        resultado  = numero1 * numero2
        st.write(f"La multiplicacion de: {numero1} X {numero2} = {resultado}")

    if seleccion == "Dividir":
        resultado  = numero1 / numero2
        st.write(f"La división de: {numero1} X {numero2} = {resultado}")

    if seleccion == "Sumar":
        resultado  = numero1 + numero2
        st.write(f"La suma de: {numero1} X {numero2} = {resultado}")

    if seleccion == "Restar":
        resultado  = numero1 - numero2
        st.write(f"La resta de: {numero1} X {numero2} = {resultado}")

if __name__ == "__main__":
    cuatro_operaciones()

# Ejercicio..2

st.subheader("Ejercicio 2: Ingresar datos de un automivil")
marca = st.text_input("Ingrese la marca del automovil")
modelo = st.text_input("Ingrese el modelo del automovil")   
kilometraje = st.number_input("Ingrese el kilometraje del automovil")

def registro_automovil():

    if st.button("Registrar datos"):
        if marca == "":
            st.write("Por favor ingrese la marca del automovil")
        elif modelo == "":
            st.write("Por favor ingrese el modelo del automovil")
        elif kilometraje == 0:
            st.write("Por favor ingrese el kilometraje ")

        st.success("Datos registrados correctaente")
        st.write(f"La marca es: {marca}")
        st.write(f"El modelo es: {modelo}")
        st.write(f"El kilometraje es: {kilometraje}")

def reiniciar_datos():
    if st.button("Borrar datos registrado"):
        marca = []
        modelo = []
        kilometraje = []
        st.success("Datos registrados borrados corectamente")

if __name__ == "__main__":
    registro_automovil()
    reiniciar_datos()

# Ejercicio..3

st.subheader("Ejercicio 3: Múltiplos de x entre 0 y 100")

# Entrada para el valor de X
x = st.number_input("Ingresa el valor de X:", min_value=1, value=1)

# Generación del array de múltiplos de X entre 0 y 100
array_multiplos = np.arange(0, 101, x)
cantidad_datos = len(array_multiplos)
sumatoria_datos = np.sum(array_multiplos)

# Mostrar resultados
st.write(f"Cantidad de datos almacenados: {cantidad_datos}")
st.write(f"Sumatoria de los datos: {sumatoria_datos}")

# Mostrar el array de múltiplos
st.write("Array de múltiplos:", array_multiplos)

# Ejercicio..4
st.subheader("Ejercicio 4: Array de Números Aleatorios entre 0 y 9")


tamaño_array = st.number_input("Ingresa el tamaño del array:", min_value=1, value=10, step=1)

# Generación del array con números aleatorios entre 0 y 9
array_numeros = np.random.randint(0, 10, tamaño_array)

# Cálculo de la media
media_valores = np.mean(array_numeros)

# Mostrar resultados
st.write("Array generado:", array_numeros)
st.write(f"Media de todos los valores: {media_valores:.2f}")

