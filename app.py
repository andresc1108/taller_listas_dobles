import streamlit as st
from doubly_linked_list import DoublyLinkedList

st.set_page_config(page_title="Taller Listas Dobles", layout="wide")

st.title("Visualizador de Listas Doblemente Enlazadas")
st.write("Implementación basada en punteros `next` y `prev`.")

# Mantener el estado de la lista en la sesión
if 'dll' not in st.session_state:
    st.session_state.dll = DoublyLinkedList()

# Sidebar: Controles de la lista
st.sidebar.header("Operaciones")
valor = st.sidebar.number_input("Valor del Nodo", value=0)
indice = st.sidebar.number_input("Índice (para Insertar/Eliminar)", min_value=0, step=1)

col1, col2 = st.sidebar.columns(2)
if col1.button("Append"):
    st.session_state.dll.append(valor)
if col2.button("Prepend"):
    st.session_state.dll.prepend(valor)

if st.sidebar.button("Insertar en Índice"):
    if not st.session_state.dll.insert(indice, valor):
        st.sidebar.error("Índice inválido")

if st.sidebar.button("Eliminar en Índice"):
    if not st.session_state.dll.remove(indice):
        st.sidebar.error("No se pudo eliminar")

# Área Principal: Visualización
st.subheader("Estado Actual de la Lista")
dll = st.session_state.dll

if dll.length == 0:
    st.info("La lista está vacía.")
else:
    # Representación visual
    nodos = []
    actual = dll.head
    while actual:
        nodos.append(f" {actual.value} ")
        actual = actual.next
    
    st.markdown("### Estructura:")
    visual_list = " <-> ".join([f"**[{n}]**" for n in nodos])
    st.write(f"NULL $\leftarrow$ {visual_list} $\rightarrow$ NULL")
    
    # Métricas técnicas
    c1, c2, c3 = st.columns(3)
    c1.metric("Tamaño (Length)", dll.length)
    c2.metric("Head", dll.head.value if dll.head else "None")
    c3.metric("Tail", dll.tail.value if dll.tail else "None")