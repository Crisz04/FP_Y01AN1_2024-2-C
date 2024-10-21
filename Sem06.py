import streamlit as st

#Título de la palicación
st.title("Ejercicios básicos con bucles en python")

#Ejercicio 1: Imprimir 10 veces 'Hola mundo'

st.subheader("Ejercicio 1: Imprimir 10 veces 'Hola mundo'")

if st.button("Ejecutar ejercicio 1"):
    for i in range(10):
        st.write("Hola Mundo")

#Ejercicio 2: Imprimir los primeros 10 numeros

st.title("Ejercicio 2: 'Imprimir los 10 primeros numeros'")

if st.button("Ejercutar ejercicio 2"):
    for i in range(1, 11):
        st.write(i)

#Ejercicio 3: Tabla de multiplicar

st.subheader("Ejercicio 3: Imprimir la tabla de multiplicar del número ingresado")

num = st.number_input("Ingrese numero")

if st.button("Ejecutar ejercicio 3"):
    for i in range(1,12):
        resultado = num * i
        st.write(f"{num} x {i} = {resultado}")
