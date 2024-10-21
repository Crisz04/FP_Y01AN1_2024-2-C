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

num = st.number_input("Ingrese numero", min_value=1)

if st.button("Ejecutar ejercicio 3"):
    for i in range(1,13):
        resultado = num * i
        st.write(f"{num} x {i} = {resultado}")


#Ejercicio 4: Calcular la media y comparar números

st.subheader("Ejercicio 4: 'Calcular la media de 10 números, saber cuantos son mayores, iguales y menores de 10'")

ingrese_numero = st.text_input("Ingrese los siguientes 10 números separados por comas: ", "12, 7, 15, 10, 20, 5, 10, 9, 8, 11")

if st.button("Ejecutar ejercicio 4"):
    lista_numeros = [int(numero) for numero in ingrese_numero.split(",")]
    media = sum(lista_numeros) / len(lista_numeros)
    mayores = len([numero for numero in lista_numeros if numero > 10])
    iguales = len([numero for numero in lista_numeros if numero == 10])
    menores = len([numero for numero in lista_numeros if numero <= 10])

    st.write(f"La media es: {media}")
    st.write(f"Los números mayores a 10 es: {mayores}")
    st.write(f"Los números iguales a 10 es: {iguales}")
    st.write(f"Los números menores a 10 es: {menores}")