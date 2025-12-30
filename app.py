import streamlit as st

# Configuración de la página sanadora
st.set_page_config(page_title="Vínculo Inteligente - Beta", page_icon="🖤", layout="wide")

# Estilo de la Caja Negra (Nada se filtra)
st.title("🖤 Vínculo Inteligente - Versión Beta")
st.info("Estás en la Caja Negra secreta. Todo el chat es libre y privado.")

# --- PARTE 1: PANEL DE CONTROL (Izquierda) ---
with st.sidebar:
    st.header("⚙️ Módulos de Guía")
    st.write("Acceso libre para los primeros 20 usuarios.")
    
    # Botones de los módulos (ahora abiertos para prueba)
    st.button("💘 Módulo Cupido")
    st.button("🤝 Terapia de Mediación")
    st.button("🚫 Ruptura Contacto Cero")
    
    st.divider()
    if st.button("🆘 BOTÓN DE PÁNICO"):
        st.error("¡PAUSA! Respira profundo, Pablo. No estás solo.")

# --- PARTE 2: EL CHAT (Centro) ---
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

# Mostrar el historial de mensajes
for m in st.session_state.mensajes:
    with st.chat_message(m["role"]):
        st.write(m["content"])

# --- PARTE 3: EL DOCTOR IA (Interacción) ---
pregunta = st.chat_input("Escribe tu mensaje aquí, Pablo...")

if pregunta:
    # Guardar mensaje del usuario
    st.session_state.mensajes.append({"role": "user", "content": pregunta})
    with st.chat_message("user"):
        st.write(pregunta)
    
    # Respuesta del Doctor IA (Simulada para la Beta)
    respuesta_doctor = f"🎙️ **Doctor IA:** Te escucho con atención, Pablo. Como estamos en la Beta, estoy analizando tu mensaje de forma sanadora para darte la mejor guía. ¿Quieres profundizar en este sentimiento?"
    
    st.session_state.mensajes.append({"role": "assistant", "content": respuesta_doctor})
    with st.chat_message("assistant"):
        st.write(respuesta_doctor)
        st.write("✨") # Emojis de aprobación
