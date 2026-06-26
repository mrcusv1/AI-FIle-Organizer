# train_model
import os
import joblib
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer

# Set the base folder that contains subfolders with files (e.g., Downloads, organized manually)
BASE_FOLDER = os.path.expanduser("organized_files_training") # You can rename this

file_names = []
categories = []

# Walk through the base folder
for category in os.listdir(BASE_FOLDER):
    category_path = os.path.join(BASE_FOLDER, category)
    if os.path.isdir(category_path):
        for file in os.listdir(category_path):
            file_path = os.path.join(category_path, file)
            if os.path.isfile(file_path):
                file_names.append(file)
                categories.append(category)

# Train the model
model = make_pipeline(CountVectorizer(), RandomForestClassifier())
model.fit(file_names, categories)

# Save the model
joblib.dump(model, "file_classifier_model.pkl")
print(f"Model trained on {len(file_names)} files and saved as file_classifier_model.pkl")
