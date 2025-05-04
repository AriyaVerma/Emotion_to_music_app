from emotion_detector import detect_emotion  # Emotion detection
from music_recommender import recommend_music  # Music recommendation based on emotion

def main():
    # Simulate emotion detection (for now hardcoded, can be dynamic later)
    emotion = "happy"  # This could come from an image, voice, or text input
    print(f"Detected Emotion: {emotion}")
    
    # Recommend music based on the detected emotion
    recommend_music(emotion)

if __name__ == "__main__":
    main()
