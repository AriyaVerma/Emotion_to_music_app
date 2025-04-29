# 🎵 Emotion-Based Music Recommendation System

A Python-based smart application that recommends songs based on your **emotions** — detected through either **text input** or **facial expressions**. This project uses **Sentiment Analysis**, **Computer Vision**, and the **Spotify API** to create a personalized and real-time music experience.


## 📌 Features

- Detects emotions from **user text input** using NLP (e.g., Hugging Face / TextBlob)
- Recognizes **facial expressions** via webcam using OpenCV and a pre-trained emotion recognition model
- Recommends music using **Spotify API** (via Spotipy) based on detected emotion
- Simple user interface using Streamlit or Tkinter (optional)
- Educational project for learning **Data Science**, **Python**, and **APIs**


## 📁 Project Structure
emotion-music-recommender/
│
├── 📁 data/              
│   └── sample_input.txt
│
├── 📁 models/                  
│   └── emotion_recognition_model.h5
│
├── 📁 src/                         # Source code for the project
│   ├── __init__.py
│   ├── main.py                    # Main script to run the app
│   ├── emotion_detector.py        # Logic for text/facial emotion detection
│   ├── music_recommender.py       # Spotify recommendation engine
│   ├── utils.py                   # Helper functions
│
├── 📁 notebooks/                  # Jupyter notebooks for exploration or EDA
│   └── emotion_analysis.ipynb
│
├── 📁 static/                     # Static files (if using web app)
│   └── images/
│       └── sample_emotions.jpg
│
├── 📁 templates/                  # HTML templates if using Flask
│   └── index.html
│
├── .gitignore                     # To ignore unnecessary files/folders
├── LICENSE                        # License (MIT or others)
├── README.md                      # Project overview and setup guide
├── requirements.txt               # List of dependencies
└── app.py                         # Entry point for the web app

## 🔧 Technologies Used

- **Python 3.8+**
- **TextBlob** or **Transformers (Hugging Face)** for sentiment analysis
- **OpenCV + Deep Learning Model** for facial emotion recognition
- **Spotipy (Spotify API)** for music recommendation
- (Optional) **Streamlit** or **Tkinter** for UI
