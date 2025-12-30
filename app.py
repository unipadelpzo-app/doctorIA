import streamlit as st
import google.generativeai as genai

# 1. Configuración del Motor (Caja Negra)
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-pro')
else:
    st.error("Falta la llave secreta en Secrets.")

# 2. Configuración de la página sanadora
st.set_page_config(page_title="Vínculo Inteligente - Beta", page_icon="🖤", layout="wide")

# Estilo visual
st.title("🖤 Vínculo Inteligente - Versión Beta")
st.info("Estás en la Caja Negra secreta. Todo el chat es libre, privado y nada será filtrado.")

# 3. PANEL DE CONTROL (Izquierda)
with st.sidebar:
    st.header("⚙️ Módulos de Guía")
    st.write("Acceso libre - Beta Test")
    
    # Botones de Módulos (Suscripción mencionada en lógica)
    if st.button("❤️ Módulo Cupido"):
        st.warning("Accediendo al Módulo Cupido ($10 USD)...")
    
    if st.button("🤝 Terapia de Mediación"):
        st.warning("Iniciando Terapia de Mediación ($10 USD)...")
        
    if st.button("🚫 Ruptura Contacto Cero"):
        st.warning("Activando Protocolo de Ruptura ($10 USD)...")
    
    st.divider()
    
    # Botón de Pánico
    if st.button("🚨 BOTÓN DE PÁNICO"):
        st.error("¡PAUSA! Respira profundo, Pablo. No estás solo. Todo va a estar bien.")

# 4. LÓGICA DEL CHAT
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Mensaje inicial del personaje
    st.session_state.messages.append({"role": "assistant", "content": "Hola, soy el Doctor IA. Estoy aquí en esta Caja Negra para escucharte de forma amable y sanadora. ¿Qué tienes en tu corazón hoy?"})

# Mostrar historial
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])

# 5. INTERACCIÓN (Entrada de usuario)
pregunta = st.chat_input("Escribe tu mensaje aquí, Pablo...")

if pregunta:
    # Mostrar mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": pregunta})
    with st.chat_message("user"):
        st.write(pregunta)
    
    # Respuesta del Doctor IA
    with st.chat_message("assistant"):
        try:
            # Instrucción de personalidad (System Prompt)
            prompt_sistema = f"Eres el Doctor IA de Vínculo Inteligente. Tu tono es sanador, amable, empático y experto en relaciones. Usa emojis de apoyo. Responde a: {pregunta}"
            
            response = model.generate_content(prompt_sistema

