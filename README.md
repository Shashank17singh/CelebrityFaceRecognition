# 🎭 Celebrity Face Recognition

A full-stack machine learning web application that detects and classifies celebrity faces from uploaded images. Built with Python, OpenCV, scikit-learn, and a Flask backend with a clean HTML/CSS/JavaScript frontend.

---

## 📌 Overview

This project uses classical computer vision and machine learning techniques to identify celebrity faces in images. The pipeline includes face detection using OpenCV's Haar Cascades, feature extraction via Wavelet Transform, and classification using a Support Vector Machine (SVM). The trained model is served through a Python Flask REST API and consumed by a responsive web UI.

---

## 🗂️ Project Structure

```
CelebrityFaceRecognition/
│
├── UI/                    # Frontend — HTML, CSS, JavaScript
├── server/                # Flask backend — REST API server
├── model/                 # Jupyter notebooks for model building & training
└── images_dataset/        # Dataset of celebrity images used for training
```

---

## ✨ Features

- Upload an image via the web interface
- Automatically detects faces in the image using OpenCV
- Predicts the celebrity identity with confidence scores
- Rejects images where a face cannot be clearly detected
- Simple, intuitive drag-and-drop UI

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python |
| Face Detection | OpenCV (Haar Cascades) |
| Feature Extraction | PyWavelets (Wavelet Transform) |
| Model | Scikit-learn (SVM / Logistic Regression) |
| Data Handling | NumPy, Pandas |
| Visualization | Matplotlib, Seaborn |
| Backend Server | Python Flask |
| Frontend | HTML, CSS, JavaScript |
| IDE | Jupyter Notebook, VS Code, PyCharm |

---

## ⚙️ Setup & Installation

### Prerequisites

- Python 3.7+
- pip

### 1. Clone the repository

```bash
git clone https://github.com/Shashank17singh/CelebrityFaceRecognition.git
cd CelebrityFaceRecognition
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

> If there is no `requirements.txt`, install the core packages manually:
> ```bash
> pip install numpy opencv-python scikit-learn matplotlib seaborn pywavelets flask
> ```

### 3. Train the model

Open and run the Jupyter notebook inside the `model/` folder step by step. This will:
- Load and preprocess images from `images_dataset/`
- Perform face detection and Wavelet feature extraction
- Train the classifier and save the model artifact

### 4. Start the Flask server

```bash
cd server
python server.py
```

The server will start at `http://localhost:5000`.

### 5. Open the UI

Open `UI/index.html` in your browser, or serve it using any static file server. Make sure the server is running before uploading images.

---

## 🚀 Usage

1. Open the web application in your browser.
2. Upload or drag-and-drop an image containing a celebrity face.
3. The app will detect the face, run it through the model, and display the predicted celebrity name along with the confidence score.

---

## 📊 Model Pipeline

```
Raw Image
    ↓
Face Detection (OpenCV Haar Cascade)
    ↓
Crop & Grayscale Conversion
    ↓
Wavelet Transform (Feature Extraction)
    ↓
SVM Classifier
    ↓
Predicted Celebrity + Confidence Score
```
