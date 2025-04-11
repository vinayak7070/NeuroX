import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

# === Load Text Dataset ===
text_df = pd.read_csv("/content/drive/MyDrive/REVEAL.AI/data/text samples dataset.csv")  # columns: title, authenticity

# === Load Image Dataset ===
if os.path.exists("/content/drive/MyDrive/REVEAL.AI/data/img.csv"):
    img_df = pd.read_csv("/content/drive/MyDrive/REVEAL.AI/data/img.csv")  # columns: img_path, Auth
elif os.path.exists("/content/drive/MyDrive/REVEAL.AI/data/imgs/img.csv"):
    img_df = pd.read_csv("/content/drive/MyDrive/REVEAL.AI/data/imgs/img.csv")  # columns: img_path, Auth
else:
    raise FileNotFoundError("Could not find 'img.csv' in either 'data' or 'data/imgs' directory.")

img_folder = "/content/drive/MyDrive/REVEAL.AI/data/imgs/"

# === Text Vectorizer Setup ===
vectorizer = TfidfVectorizer()
X_text = vectorizer.fit_transform(text_df['title'])

# === Text-Based Question Authenticity Check ===
def check_text_authenticity(question):
    q_vec = vectorizer.transform([question])
    similarities = cosine_similarity(q_vec, X_text).flatten()
    best_match_idx = similarities.argmax()

    matched_title = text_df.iloc[best_match_idx]['title']
    authenticity = text_df.iloc[best_match_idx]['authenticity']
    score = similarities[best_match_idx]

    print("\n🧠 TEXT ANALYSIS RESULT:")
    print(f"📌 Closest Match: {matched_title}")
    print(f"🔍 Similarity Score: {score:.2f}")
    print(f"✅ Verdict: {authenticity.upper()}")

    return matched_title, authenticity, score  # ✅ FIXED: returning 3 values

# === Image-Based Authenticity Check ===
def check_image_authenticity(image_filename):
    if image_filename not in img_df['img_path'].values:
        print("\n🖼️ IMAGE ANALYSIS RESULT:")
        print("⚠️ Image not found in dataset.")
        return "unknown"

    result = img_df[img_df['img_path'] == image_filename]['Auth'].values[0]
    print("\n🖼️ IMAGE ANALYSIS RESULT:")
    print(f"🖼️ Image: {image_filename}")
    print(f"✅ Verdict: {result.upper()}")
    return result

# === Combined (Optional CLI-style) Function ===
def analyze_input(question=None, image_filename=None):
    print("======================================")
    if question:
        check_text_authenticity(question)
    if image_filename:
        check_image_authenticity(image_filename)
    print("======================================\n")
