# Chatbot de Fórmula 1 — Streamlit + Groq + FastF1

Um chatbot sobre Fórmula 1, desenvolvido com **Groq (Llama 3.1)**,
**Streamlit** para interface e **FastF1** para dados reais da categoria.

Este projeto permite perguntar sobre corridas, pilotos, estatísticas, tempos de volta e informações técnicas da F1.

---

## Demonstração
**

---

## Funcionalidades

- Responde perguntas gerais sobre Fórmula 1 usando IA  
- Consulta resultados da última corrida  
- Obtém tempos de volta de pilotos usando FastF1  
- Exibe informações de GPs (ano, local, data)  
- Interface visual customizada (tema F1 vermelho/preto)  

---

## Estrutura do Projeto
Chatbot_F1/
│── app.py |
│── utils_f1.py |
│── style.css |  
│── header.html |
│── cache/ | 
│── .env | 

---

## Tecnologias

| Tecnologia |
|-----------|
| **Python** | 
| **Streamlit** |
| **Groq API (Llama 3.1)** |
| **FastF1** |
| **HTML + CSS** |

## Instalação

Clone o repositório:

```bash
git clone https://github.com/DITTOio/Chatbot_F1.git
cd Chatbot_F1

```
Instale as dependências:
```bash
pip install streamlit groq python-dotenv fastf1 requests pandas numpy matplotlib
```



## Configuração da API Groq

Crie o arquivo .env na raiz do projeto:

```bash
GROQ_API_KEY=sua_chave_aqui
```
A chave pode ser criada gratuitamente em:
https://console.groq.com/keys

## Como rodar o projeto

Execute:
```bash
python -m streamlit run app.py
-----
streamlit run app.py
```
Acesse no navegador:
http://localhost:8501/
