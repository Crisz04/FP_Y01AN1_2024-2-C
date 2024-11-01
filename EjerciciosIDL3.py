#EJERCICIOS PARA EL IDL3
import streamlit as st
st.title("EJERCICIOS PROPUESTOS PARA EL CASO PROPUESTO IDL 3")

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
    if st.button("Reiniciar datos"):
        marca = []
        modelo = []
        kilometraje = []

if __name__ == "__main__":
    registro_automovil()
    reiniciar_datos()
    

   
