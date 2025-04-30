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
├── data/  
│   └── sample_input.txt  
├── models/  
│   └── emotion_recognition_model.h5  
├── src/  
│   ├── __init__.py  
│   ├── main.py  
│   ├── emotion_detector.py  
│   ├── music_recommender.py  
│   └── utils.py  
├── notebooks/  
│   └── emotion_analysis.ipynb  
├── static/  
│   └── images/  
│       └── sample_emotions.jpg  
├── templates/  
│   └── index.html  
├── .gitignore  
├── LICENSE  
├── README.md  
├── requirements.txt  
└── app.py  




## 🔧 Technologies Used

- **Python 3.8+**
- **TextBlob** or **Transformers (Hugging Face)** for sentiment analysis
- **OpenCV + Deep Learning Model** for facial emotion recognition
- **Spotipy (Spotify API)** for music recommendation
- (Optional) **Streamlit** or **Tkinter** for UI

## How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/AriyaVerma/emotion-music-recommender.git
   cd emotion-music-recommender
2. **Create and activate a virtual environment**


3. **Install dependencies**
4. **Run the app**
5. **Visit**




## 📚 Future Enhancements

- Support for voice-based emotion detection.
- Integration with other streaming platforms (YouTube Music, Apple Music).
- Mobile app version.

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

