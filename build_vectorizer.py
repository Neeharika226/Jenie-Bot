import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import pickle

# Load cleaned patterns
df = pd.read_csv("patterns.csv")

# Fit vectorizer
vectorizer = CountVectorizer()
vectorizer.fit(df["cleaned_pattern"])

# Save the vectorizer
with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ vectorizer.pkl created successfully!")
