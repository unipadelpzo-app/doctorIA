import streamlit as st
import google.generativeai as genai

# 1. CONEXIÓN AL MOTOR (LA LLAVE MAESTRA)
if "GOOGLE_API_KEY" in st.secrets:
    # Configuramos la llave eliminando cualquier espacio accidental
    api_key = st.secrets["GOOGLE_API_KEY"].strip()
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
else:
    st.error("⚠️ Error: No encuentro la llave API en Secrets.")

# 2. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(page_title="Vínculo Inteligente - Doctor IA", page_icon="🖤")

st.title("🖤 Vínculo Inteligente - Doctor IA")
st.write("Bienvenido a tu espacio privado. Aquí nada se filtra y todo es confidencial.")

# 3. BARRA LATERAL (MÓDULOS PREMIUM Y PÁNICO)
with st.sidebar:
    st.header("⚙️ Menú de Guía")
    st.button("❤️ Módulo Cupido")
    st.button("🤝 Terapia de Mediación")
    st.button("🚫 Ruptura Contacto Cero")
    st.divider()
    if st.button("🚨 BOTÓN DE PÁNICO"):
        st.error("¡PAUSA! Respira profundo. Este es un espacio seguro.")

# 4. SISTEMA DE CHAT (Lógica de Identidad)
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Saludo universal, amable y sanador
    st.session_state.messages.append({"
