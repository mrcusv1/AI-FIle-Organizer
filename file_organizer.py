# ml_file_organizer.py
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import shutil
import joblib

# Load the trained model
model = joblib.load("file_classifier_model.pkl")

# Base folder categories
CATEGORIES = ["Documents", "Pictures", "Entertainment", "Music", "Archives", "Other"]

# Predict category using ML model
def predict_category(file_name):
    return model.predict([file_name])[0]

# Event handler
class FileOrganizerHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            file_path = event.src_path
            file_name = os.path.basename(file_path)
            
            # Predict category using ML
            predicted_folder = predict_category(file_name)
            
            # Fallback if not in defined categories
            if predicted_folder not in CATEGORIES:
                predicted_folder = "Other"
                
            # Move file
            destination_path = os.path.join(os.path.dirname(file_path), predicted_folder)
            if not os.path.exists(destination_path):
                os.makedirs(destination_path)
                
            shutil.move(file_path, os.path.join(destination_path, file_name))
            print(f"Moved {file_name} to {predicted_folder}")

# Main
if __name__ == "__main__":
    directory_to_monitor = os.path.expanduser("Test_folderr")
    
    event_handler = FileOrganizerHandler()
    observer = Observer()
    observer.schedule(event_handler, path=directory_to_monitor, recursive=False)
    observer.start()
    
    try:
        print(f"Monitoring {directory_to_monitor} for new files...")
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
