#EJERCICIOS PARA EL CASO PROPUESTO IDL3
import streamlit as st

st.title("EJERCICIOS PROPUESTOS PARA EL CASO PROPUESTO IDL 3")
st.subheader("Ejercicio 1: Calculadora con las cuatro operaciones")

<<<<<<< HEAD
numero1 = st.number_input("Ingrese primer número a operar", min_value = 1)
numero2 = st.number_input("Ingrese segundo número a operar", min_value = 1)
st.write("Selecciona una de las 4 operaciones")
menus = ["Multiplicar","Dividir","Sumar","Restar"]
seleccion = ""
seleccion = st.radio("4 operaciones", menus)

def sumar():
    resultado = numero1 + numero2
    print(f"El resultado de la suma de es: {numero1} + {numero2} = {resultado}")

def restar():
    resultado = numero1 - numero2
    print(f"El resultado de la resta de es: {numero1} - {numero2} = {resultado}")

def multiplicar():
    resultado = numero1 * numero2
    print(f"El resultado de la multiplicación de es: {numero1} x {numero2} = {resultado}")

def dividir():
    resultado = numero1 / numero2
    print(f"El resultado de la división de es : {numero1} / {numero2} = {resultado}")


if seleccion == "Multiplicar":
    multiplicar()
elif seleccion == "Dividir":
    dividir()
elif seleccion == "Sumar":
    sumar()
elif seleccion == "Restar":
    restar()