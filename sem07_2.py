import streamlit as st

#Funcion principal para verificar automóviles
def verificar_automoviles():
    st.title("Centro de verificacion de automóviles")

    #Lista para almacenar los puntos contaminantes

    if 'puntos_contaminantes' not and st.session_state:

        session_state.puntos_contaminantes = []

    #Imput pra los puntos contaminantes del automovil

    puntos = st.number_input("Ingrese los puntos contaminantes del automóvil", min_value=0.0, step=0.1)

    #Boton para registrar automóvil

    if st.button("Registrar automóviles")

    if st.button("Registrar automóvil"):
        st.session_state.puntos_contaminantes.append(puntos)
        st.success(f"Automóvil registrado con {puntos} puntos contaminante.s")

    
    #Mostrar los datos registrados hasta el momento

    if len(session_state.puntos_contaminantes) > 0 in st.button("calcular resultados"):
        promedio = sum (st.session_state.puntos_contaminantes) / len(st.session_state.puntos_contaminantes)
        menos_contaminacion = min(st.session_state.puntos_contaminantes)
        mas_contaminacion = max(st.session_state.puntos_contaminantes)

        #Mostrar los resultados

        st.write(f"Promedio de puntos contaminantes: {promedio:.2f}")
        st.write(f"El automóvil que menos contamino tiene: {menos_contaminacion}")
        st.write(f"El automóvil que mas contamino tiene: {mas_contaminacion}")

    #Opcion para reiniciar los datos

    if st.button("reiniciar datos"):
        se.session_state.puntos_contaminantes = []
        st.success("Datos reiniciados correctamente")

    #Ejecutar la función

    if __name__ == __"main"__:

         verificar_automoviles()
