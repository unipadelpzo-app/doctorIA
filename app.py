import streamlit as st
import google.generativeai as genai

# 1. Conexión al motor de IA (Tu llave secreta)
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-pro')
else:
    st.error("⚠️ Error: No se encuentra la llave en Secrets.")

# 2. Configuración de la interfaz sanadora
st.set_page_config(page_title="Vínculo Inteligente", page_icon="🖤", layout="wide")

st.title("🖤 Vínculo Inteligente - Caja Negra")
st.markdown("---")

# 3. Panel Lateral con Módulos Premium
with st.sidebar:
    st.header("⚙️ Menú de Guía")
    
    # Módulos de pago ($10 USD)
    if st.button("❤️ Módulo Cupido"):
        st.info("Iniciando Módulo Cupido... ($10 USD/mes)")
    if st.button("🤝 Terapia de Mediación"):
        st.info("Iniciando Mediación... ($10 USD/mes)")
    if st.button("🚫 Ruptura Contacto Cero"):
        st.info("Iniciando Plan de Ruptura... ($10 USD/mes)")
        
    st.divider()
    
    # Botón de Pánico
    if st.button("🚨 BOTÓN DE PÁNICO"):
        st.error("¡ALTO! Respira profundo. No tomes decisiones impulsivas ahora.")

# 4. Lógica del Chat del Doctor IA
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar el historial
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])

# Entrada de usuario
pregunta = st.chat_input("Escribe tu mensaje aquí, Pablo...")

if pregunta:
    # Guardar mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": pregunta})
    with st.chat_message("user"):
        st.write(pregunta)
    
    # Respuesta REAL del motor
    with st.chat_message("assistant"):
        try:
            # Instrucción de personalidad sanadora y amable
            contexto = "Eres el Doctor IA de Vínculo Inteligente. Responde con mucha empatía, de forma sanadora, amable y breve. Valida los sentimientos del usuario con emojis."
            full_prompt = f"{contexto}\nUsuario dice: {pregunta}"
            
            # Aquí es donde ocurre la magia (El motor responde)
            response = model.generate_content(full_prompt)
            respuesta_doctor = response.text
            
            st.write(respuesta_doctor)
            st.session_state.messages.append({"role": "assistant", "content": respuesta_doctor})
        except Exception as e:
            st.error("El Doctor IA está fuera de línea. Revisa tu llave API en Secrets.")
