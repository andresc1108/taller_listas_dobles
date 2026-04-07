import streamlit as st
from vital_history import VitalHistory
from vital_sign import VitalSign

st.set_page_config(page_title="Monitor Médico - UCC", layout="wide")
st.title("🏥 Historial de Signos Vitales (Lista Doble)")

if 'history' not in st.session_state:
    st.session_state.history = VitalHistory()

with st.sidebar:
    st.header("Nuevo Registro")
    hr = st.number_input("Frecuencia Cardíaca", 40, 200, 75)
    bp = st.text_input("Presión Arterial", "120/80")
    ox = st.number_input("Oxigenación %", 50, 100, 98)
    if st.button("Guardar"):
        st.session_state.history.add_record(VitalSign(hr, bp, ox))

hist = st.session_state.history
if hist.length == 0:
    st.info("No hay registros médicos.")
else:
    curr = hist.head
    idx = 0
    while curr:
        st.write(f"**Registro #{idx}** - {curr.data}")
        if st.button(f"Eliminar {idx}", key=f"btn_{idx}"):
            hist.remove_record(idx)
            st.rerun()
        curr = curr.next
        idx += 1