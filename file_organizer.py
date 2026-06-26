import os
import shutil
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Sample dataset (file names and categories)
data = [
    ("photo.jpg", "Pictures"),
    ("music.mp3", "Entertainment"),
]

# Extract features (file name length + extension encoding)
def extract_features(file_name):
    name_length = len(file_name)
    extension = file_name.split(".")[-1]
    extension_mapping = {"exe": 0, "mp4": 1, "jpg": 2, "png": 3, "mp3": 4}
    return [name_length, extension_mapping.get(extension, -1)]

# Prepare data for training
file_names, labels = zip(*data)
label_encoder = LabelEncoder()
encoded_labels = label_encoder.fit_transform(labels)
features = np.array([extract_features(f) for f in file_names])
X_train, X_test, y_train, y_test = train_test_split(features, encoded_labels, test_size=0.2, random_state=42)

# Build AI Model
model = Sequential([
    Dense(16, activation='relu', input_shape=(2,)),
    Dense(8, activation='relu'),
    Dense(len(set(encoded_labels)), activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, batch_size=2, verbose=1)

# Function to predict category
def predict_category(file_name):
    feature = np.array([extract_features(file_name)])
    prediction = model.predict(feature, verbose=0)
    return label_encoder.inverse_transform([np.argmax(prediction)])[0]

# Organize files into folders
def organize_files(file_list, base_directory):
    for file in file_list:
        def organize_files(file_list, base_directory):
         category = predict_category(file)
        category_path = os.path.join(base_directory, category)
        os.makedirs(category_path, exist_ok=True)
        file_path = os.path.join(base_directory, file)
        new_path = os.path.join(category_path, file)
        if os.path.exists(file_path):
            shutil.move(file_path, new_path)
            print(f"Moved {file} to {category}/")
            print("Detected files:", file_list)
        else:
            print(f"File {file} not found in the base directory.")

# Run the script
if __name__ == "__main__":
    new_files = ["Entertainment", "Pictures"]
    base_directory = "./files"
    organize_files(new_files, base_directory)
