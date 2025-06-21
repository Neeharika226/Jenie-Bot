import eel
import json
import pandas as pd
import string
import pickle
import random
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Initialize Eel
eel.init('web')

# Load intents
with open('intents.json', 'r') as f:
    intents = json.load(f)

# Load vectorizer
with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Load pattern dataset
df = pd.read_csv('patterns.csv')

# Preprocessing function
def preprocess(text):
    text = text.lower()
    return text.translate(str.maketrans('', '', string.punctuation))

# Chat function exposed to JS
@eel.expose
def get_bot_response(user_input):
    user_input_clean = preprocess(user_input)
    user_vec = vectorizer.transform([user_input_clean])
    pattern_vecs = vectorizer.transform(df['cleaned_pattern'])
    similarity = cosine_similarity(user_vec, pattern_vecs)

    max_idx = np.argmax(similarity)
    max_score = similarity[0][max_idx]

    if max_score < 0.3:
        return "Sorry, I didn't understand that. Please ask a Python-related question."

    tag = df.iloc[max_idx]['tag']
    for intent in intents['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])


eel.start('index.html', size=(700, 600), mode=None)


try:
    eel.start('index.html', size=(700, 600))
except (SystemExit, MemoryError, KeyboardInterrupt):
    print("Exited")
except Exception as e:
    print("Error while starting Eel:", e)

