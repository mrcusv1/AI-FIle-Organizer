***Summary***
AI File Organizer

Link to the research paper: https://docs.google.com/document/d/1zWwrqLUhDA3_IMMzyrJRG43sns2idvM6lOZC6XeBtao/edit?usp=sharing

A smart background automation tool that uses a Machine Learning classifier to instantly
sort newly added files into dedicated category folders based on their file names.

---

**Features**
* **Live File System Monitoring:** Uses `watchdog` to detect new files the exact second they hit your target folder.
* **AI Classification:** Leverages a `RandomForestClassifier` and text vectorization to accurately predict file categories.
* **Smart Fallbacks:** Dynamically creates folders on-the-fly and drops unknown file types safely into an `Other/` directory.

---
### 1. Prerequisites
Make sure you have Python installed, then install the required automation and machine learning libraries:
```bash
pip install scikit-learn joblib watchdog
```

### 2. Step 1: Train the AI Model
Before running the organizer, you must train the model so it learns your file layout rules. 
1. Place a few example files into organized subfolders within a directory named `organized_files_training` (e.g., put PDFs in a `Documents` folder).
2. Run the training script:
   ```bash
   python train_model.py
   ```
This generates a `file_classifier_model.pkl` file in your root directory.

### 3. Step 2: Start the Live Monitor
Once your model is trained, start the organizer script to begin watching your target directory (default: `Test_folder`):
```bash
python ml_file_organizer.py
```
Leave this terminal window open. Any new file you drop into that folder will be sorted instantly!

---

## 📂 Project Structure
* **`train_model.py`** — Parses your training directories and trains the Random Forest classifier.
* **`ml_file_organizer.py`** — The main background service monitoring file system events.
* **`models/`** — Recommended folder to store your trained `.pkl` models.
