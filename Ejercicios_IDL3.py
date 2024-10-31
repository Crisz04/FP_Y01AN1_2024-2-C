#EJERCICIOS PARA EL CASO PROPUESTO IDL3
import streamlit as st
def operaciones():
    st.title("EJERCICIOS PROPUESTOS PARA EL CASO PROPUESTO IDL 3")
    st.subheader("Ejercicio 1: Calculadora con las cuatro operaciones")
    numero1 = st.number_input("Ingrese primer número a operar", min_value = 1)
    numero2 = st.number_input("Ingrese segundo número a operar", min_value = 1)
    st.write("Selecciona una de las 4 operaciones")
    menus = ["Multiplicar","Dividir","Sumar","Restar"]
    seleccion = ""
    seleccion = st.radio("4 operaciones", menus) 

    if seleccion == "Multiplicar":
        resultado = numero1 + numero2
        print(f"El resultado de la suma de es: {numero1} x {numero2} = {resultado}")
        st.write("Multiplicar")
    elif seleccion == "Dividir":
        resultado = numero1 + numero2
        print(f"El resultado de la suma de es: {numero1} / {numero2} = {resultado}")
        st.write("Dividir")
if __name__ == "__main__":
    operaciones()