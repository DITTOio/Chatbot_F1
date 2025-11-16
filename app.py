import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq
from utils_f1 import (
    get_last_race_results,
    get_driver_lap_times,
    get_race_info
)

# CONFIG
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    st.error("ERROR:Crie um arquivo .env com: GROQ_API_KEY=sua_chave")
    st.stop()

client = Groq(api_key=API_KEY)

# FUNÇÃO IA

def ask_groq(message):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "Você é um especialista em Fórmula 1. Responda sempre em português."},
            {"role": "user", "content": message}
        ],
        temperature=0.6,
        max_tokens=300
    )
    return response.choices[0].message.content


# LOGICA DO BOT

def process_message(msg):
    msg_lower = msg.lower()

    if "última corrida" in msg_lower or "ultima corrida" in msg_lower:
        return get_last_race_results()

    if "voltas" in msg_lower:
        try:
            tokens = msg.split()
            year = int(tokens[-3])
            gp = tokens[-2]
            driver = tokens[-1].upper()
            return get_driver_lap_times(year, gp, driver)
        except:
            return "Formato correto: `voltas 2024 Bahrain VER`"

    if "info" in msg_lower or "informações" in msg_lower:
        try:
            tokens = msg.split()
            year = int(tokens[-2])
            gp = tokens[-1]
            return get_race_info(year, gp)
        except:
            return "Formato correto: `info 2024 Monza`"

    return ask_groq(msg)


# CSS EXTERNO
def load_css(file_name):
    with open(file_name, encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("style.css")

# HEADER HTML
def load_html(file_name):
    with open(file_name, encoding="utf-8") as f:
        st.markdown(f.read(), unsafe_allow_html=True)

load_html("header.html")

# INTERFACE

with st.container():
    st.markdown('<div class="main-box">', unsafe_allow_html=True)

    msg = st.text_input("Digite sua pergunta:")

    if st.button("Enviar"):
        resposta = process_message(msg)
        st.markdown(f'<div class="answer-box">{resposta}</div>', unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

