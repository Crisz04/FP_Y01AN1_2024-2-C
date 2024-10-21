import streamlit as st

#Título de la palicación
st.title("Ejercicios básicos con bucles en python")

#Ejercicio 1: Imprimir 10 veces 'Hola mundo'

st.subheader("Ejercicio 1: Imprimir 10 veces 'Hola mundo'")

if st.button("Ejecutar ejercicio 1"):
    for i in range(10):
        st.write("Hola Mundo")