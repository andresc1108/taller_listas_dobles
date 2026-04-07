import streamlit as st
from vital_history import VitalHistory
from vital_sign import VitalSign

st.set_page_config(page_title="Monitor Médico", layout="wide")

# Diccionario de Iconos SVG
SVG = {
    "activity": '<svg viewBox="0 0 24 24" width="30" height="30" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>',
    "heart": '<svg viewBox="0 0 24 24" width="24" height="24" stroke="#FF4B4B" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>'
}

st.markdown("""
    <style>
    .card { border-radius: 12px; padding: 20px; background: #ffffff; border: 1px solid #e6e9ef; border-left: 6px solid #007bff; margin-bottom: 15px; box-shadow: 2px 2px 5px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

if 'history' not in st.session_state:
    st.session_state.history = VitalHistory()

# Encabezado
c1, c2 = st.columns([0.05, 0.95])
with c1: st.write(SVG["activity"], unsafe_allow_html=True)
with c2: st.title("Dashboard de Signos Vitales.")

# Panel de control
with st.sidebar:
    st.header("Captura de Datos")
    hr = st.slider("Frecuencia Cardíaca (bpm)", 40, 180, 80)
    ox = st.slider("Oxigenación (%)", 80, 100, 97)
    bp = st.text_input("Presión Arterial", "120/80")
    
    col1, col2 = st.columns(2)
    if col1.button("Final (Append)"): st.session_state.history.append(VitalSign(hr, bp, ox))
    if col2.button("Inicio (Prepend)"): st.session_state.history.prepend(VitalSign(hr, bp, ox))
    
    idx = st.number_input("Posición de Inserción", 0, st.session_state.history.length, 0)
    if st.button("Insertar por Índice"):
        st.session_state.history.insert(idx, VitalSign(hr, bp, ox))

# Visualización
hist = st.session_state.history
if hist.length > 0:
    last = hist.tail.data
    status, color = last.get_health_status()
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Pulso Actual", f"{last.heart_rate} bpm")
    m2.metric("SpO2 Actual", f"{last.oxygen}%")
    m3.metric("Estado", status)

    st.divider()
    st.subheader("Línea de Tiempo")
    modo = st.toggle("Recorrido Inverso (Tail -> Head)")
    
    curr = hist.tail if modo else hist.head
    i = hist.length - 1 if modo else 0
    
    while curr:
        s_lbl, s_col = curr.data.get_health_status()
        st.markdown(f"""
            <div class="card" style="border-left-color: {s_col};">
                <div style="display: flex; justify-content: space-between;">
                    <span style="font-weight: bold; color: {s_col};">{s_lbl}</span>
                    <span style="color: gray;">{curr.data.timestamp}</span>
                </div>
                <h4 style="margin: 10px 0;">Registro #{i}</h4>
                <p><b>FC:</b> {curr.data.heart_rate} bpm | <b>PA:</b> {curr.data.blood_pressure} | <b>SpO2:</b> {curr.data.oxygen}%</p>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button(f"Eliminar {i}", key=f"del_{i}"):
            hist.remove(i)
            st.rerun()
            
        curr = curr.prev if modo else curr.next
        i = i - 1 if modo else i + 1
else:
    st.info("Ingresa datos para comenzar el monitoreo.")