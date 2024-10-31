#EJERCICIOS PARA EL CASO PROPUESTO IDL3
import streamlit as st

st.title("EJERCICIOS PROPUESTOS PARA EL CASO PROPUESTO IDL 3")
st.subheader("Ejercicio 1: Crear una calculadora de las cuatro operaciones básicas, donde se envíe los parámetros a operar y este retorne los resultados")
st.subheader("Ejercicio 1: Calculadora con las cuatro operaciones")
numero1 = st.number_input("Ingrese primer número a operar", min_value = 1)
numero2 = st.number_input("Ingrese segundo número a operar", min_value = 1)
st.write("Selecciona una de las 4 operaciones")
menus = ["Multiplicar","Dividir","Sumar","Restar"]
seleccion = ""
seleccion = st.radio("4 operaciones", menus)

def cuatro_operaciones()
    if seleccion == "Multiplicar"
        resultado  = numero1 * numero2
        st.write(f"La multiplicacion de {numero1} X {numero2} = {resultado}")

    if seleccion == "Dividir"
        resultado  = numero1 / numero2
        st.write(f"La división de : {numero1} X {numero2} = {resultado}")

if __name__ == "__main__":
    cuatro_operaciones()