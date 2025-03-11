pip install streamlit pillow
import streamlit as st
from PIL import Image
import random

# Charger des images pour illustrer la conversation
images = {
    "customer": "https://www.pngall.com/wp-content/uploads/5/Customer-PNG.png",
    "store": "https://www.pngall.com/wp-content/uploads/4/Store-PNG-Picture.png",
    "assistant": "https://www.pngall.com/wp-content/uploads/5/Assistant-PNG-Clipart.png",
}

# Fonction pour afficher une image avec texte
def display_message(sender, text, img_url):
    col1, col2 = st.columns([1, 5])
    with col1:
        st.image(img_url, width=60)
    with col2:
        st.markdown(f"**{sender}:** {text}")

# Initialisation de l'historique de conversation
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Titre et image de bienvenue
st.title("🛍️ AI Store Assistant - Interactive Chat")
st.image(images["store"], width=400)
st.write("Welcome! You are the salesperson. Chat with the customer and assist them.")

# Interface du chat
for chat in st.session_state.chat_history:
    display_message(chat["sender"], chat["message"], chat["image"])

# Entrée utilisateur (simulateur de conversation)
user_input = st.text_input("Type your response...", key="user_input")

# Réponses dynamiques générées par l’IA
def generate_ai_response(user_text):
    responses = [
        "Of course! What type of product are you looking for?",
        "We have different sizes and styles available. Would you like recommendations?",
        "This item is on sale today! Special discount for you.",
        "You can pay at the front desk or through our mobile app.",
        "Is there anything else I can help you with?",
        "Thank you for visiting our store! Have a great day!"
    ]
    return random.choice(responses)

# Soumission de la réponse
if st.button("Send"):
    if user_input.strip():
        # Ajout du message de l'utilisateur
        st.session_state.chat_history.append({"sender": "You", "message": user_input, "image": images["customer"]})

        # Génération de la réponse AI
        ai_response = generate_ai_response(user_input)
        st.session_state.chat_history.append({"sender": "Assistant", "message": ai_response, "image": images["assistant"]})

        # Actualisation de la page
        st.rerun()
