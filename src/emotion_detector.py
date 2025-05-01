from transformers import pipeline

emotion_pipeline = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=False)

def detect_emotion(text):
    try:
        result = emotion_pipeline(text)
        emotion = result[0]['label']
        return emotion
    except Exception as e:
        print("Error detecting emotion:", e)
        return "neutral"

if __name__ == "__main__":
    text = input("Enter how you feel: ")
    emotion = detect_emotion(text)
    print("Detected Emotion:", emotion)
