import streamlit as st
def mostar_menu():
    st.title("Ejemplo de menu")
    st.write("selecciona una opcion del menú")

    menus = ["archivo", "Editar", "Ver", "Salir"]
    seleccion = ""

    while seleccion != "salir":
        seleccion = st.radio("Menu", menu)

        if seleccion == "Archivo":
            st.write("Seleccionaste Archivo")
        elif seleccion == "Editar":
            st.write("Seleccionaste editar")
        elif seleccion == "Ver":
            st.write("Seleccionaste: Ver")
        elif seleccion == "Salir":
            st.write("¡Saliendo sel Menu!")
            break

if __name__ == "__main__":
    mostar_menu()
