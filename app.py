import streamlit as st
import google.generativeai as genai

# 1. CONEXIÓN AL MOTOR (LA LLAVE MAESTRA)
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-pro')
else:
    st.error("⚠️ Error: No encuentro la llave API en Secrets.")

# 2. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(page_title="Vínculo Inteligente", page_icon="🖤", layout="wide")

st.title("🖤 Vínculo Inteligente - Doctor IA")
st.write("Bienvenido a tu espacio privado. Aquí nada se filtra y todo es confidencial.")

# 3. BARRA LATERAL (MÓDULOS PREMIUM Y PÁNICO)
with st.sidebar:
    st.header("⚙️ Menú de Guía")
    # Los módulos requieren suscripción mensual según reglas de negocio
    st.button("❤️ Módulo Cupido")
    st.button("🤝 Terapia de Mediación")
    st.button("🚫 Ruptura Contacto Cero")
    st.divider()
    if st.button("🚨 BOTÓN DE PÁNICO"):
        st.error("¡PAUSA! Respira profundo. Este es un espacio seguro. No estás solo.")

# 4. SISTEMA DE CHAT (Lógica de Identidad)
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Saludo universal sin nombres fijos
    st.session_state.messages.append({"role": "assistant", "content": "Hola, soy el Doctor IA. Te escucho con total atención y sin juicios en esta Caja Negra. ¿Qué traes en tu corazón hoy?"})

# Mostrar historial
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])

# 5. ENTRADA DE TEXTO
pregunta = st.chat_input("Escribe tu mensaje aquí...")

if pregunta:
    st.session_state.messages.append({"role": "user", "content": pregunta})
    with st.chat_message("user"):
        st.write(pregunta)
    
    with st.chat_message("assistant"):
        try:
            # Instrucción para que la IA sea empática y no asuma nombres
            instruccion = (
                "Eres el Doctor IA de Vínculo Inteligente. Tu tono es sanador, amable y experto. "
                "No uses el nombre 'Pablo' a menos que el usuario te diga que se llama así. "
                "Valida los sentimientos del usuario con emojis y responde de forma breve y profunda."
            )
            
            response = model.generate_content(f"{instruccion}\nUsuario: {pregunta}")
            respuesta_real = response.text
            
            st.write(respuesta_real)
            st.session_state.messages.append({"role": "assistant", "content": respuesta_real})
            
        except Exception as e:
            st.error("El Doctor IA está procesando mucha información. Revisa la conexión del motor.")
