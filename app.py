import os
import streamlit as st
from openai import OpenAI
from utils_f1 import (
    get_last_race_results,
    get_driver_lap_times,
    get_race_info,
)
from dotenv import load_dotenv
import os

load_dotenv()  # carrega o .env

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ---------------------------
# INTERFACE
# ---------------------------
st.set_page_config(page_title="Chatbot de Fórmula 1", page_icon="🏎️")

st.title("🏎️ Chatbot de Fórmula 1 — FastF1 + OpenAI")

st.write("Faça uma pergunta sobre Fórmula 1! Exemplos:")
st.code("""
última corrida
voltas 2024 Bahrain VER
info 2024 Monza
quem é o melhor piloto de chuva?
""")


# ---------------------------
# OPENAI CLIENT
# ---------------------------
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    st.error("⚠️ Coloque sua chave no .env ou exporte OPENAI_API_KEY")
else:
    client = OpenAI(api_key=OPENAI_API_KEY)


# ---------------------------
# PROCESSAMENTO DA MENSAGEM
# ---------------------------
def ask_openai(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é um especialista em Fórmula 1. Responda de forma simples e clara."},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message["content"]


def process_user_message(msg):
    msg_lower = msg.lower()

    # Última corrida
    if "última corrida" in msg_lower or "ultima corrida" in msg_lower:
        return get_last_race_results()

    # Tempos de volta
    if "voltas" in msg_lower:
        try:
            tokens = msg.split()
            year = int(tokens[-3])
            gp = tokens[-2]
            driver = tokens[-1].upper()
            return get_driver_lap_times(year, gp, driver)
        except:
            return "Formato correto: `voltas 2024 Bahrain VER`"

    # Info de GP
    if "info" in msg_lower:
        try:
            tokens = msg.split()
            year = int(tokens[-2])
            gp = tokens[-1]
            return get_race_info(year, gp)
        except:
            return "Formato correto: `info 2024 Monza`"

    # Caso contrário: OpenAI responde
    return ask_openai(msg)


# ---------------------------
# CHAT
# ---------------------------
user_input = st.text_input("Digite sua pergunta:")

if st.button("Enviar"):
    if user_input.strip() == "":
        st.warning("Digite alguma coisa 😅")
    else:
        resposta = process_user_message(user_input)
        st.success("Resposta:")
        st.write(resposta)
