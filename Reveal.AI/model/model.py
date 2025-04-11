import pandas as pd
import cv2
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Load image label CSV
img_df = pd.read_csv("image/finalimg.csv")

# Step 1: Load images & labels
X_images = []
y_labels = []

for index, row in img_df.iterrows():
    img_path = os.path.join("image", row["img_path"])
    label = 1 if row["authenticity"].strip().lower() == "real" else 0

    # Read and resize image
    img = cv2.imread(img_path)
    if img is not None:
        img = cv2.resize(img, (64, 64))  # You can change size
        img_flat = img.flatten()
        X_images.append(img_flat)
        y_labels.append(label)

# Convert to numpy
X = np.array(X_images)
y = np.array(y_labels)

# Step 2: Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 3: Train
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Step 4: Evaluate
y_pred = model.predict(X_test)
print("🎯 Image Classifier Accuracy:", accuracy_score(y_test, y_pred))
print("📊 Classification Report:\n", classification_report(y_test, y_pred))

# Step 5: Save model
joblib.dump(model, "revealai_image_model.pkl")

print("✅ Image fake/real model saved successfully!")
