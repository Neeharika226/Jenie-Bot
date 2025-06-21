import json
import pandas as pd
import string

# Load intents
with open("intents.json") as file:
    intents = json.load(file)

# Clean text: lowercase and remove punctuation
def preprocess(text):
    text = text.lower()
    return text.translate(str.maketrans('', '', string.punctuation))

# Create a list of all pattern–tag pairs
data = []
for intent in intents["intents"]:
    tag = intent["tag"]
    for pattern in intent["patterns"]:
        cleaned = preprocess(pattern)
        data.append({"pattern": pattern, "cleaned_pattern": cleaned, "tag": tag})

# Convert to DataFrame and save
df = pd.DataFrame(data)
df.to_csv("patterns.csv", index=False)

print("✅ patterns.csv created successfully!")
