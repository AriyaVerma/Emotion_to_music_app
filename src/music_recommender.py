from emotion_detector import detect_emotion  # Import emotion detection module
from spotify_helper import get_tracks_by_emotion  # Import the function to get tracks based on emotion

def recommend_music(emotion):
    """
    Function to recommend music based on the detected emotion.
    It fetches tracks from Spotify based on the emotion.
    """
    print(f"Recommending music for the emotion: {emotion}")

    # Fetch music recommendations from Spotify using the emotion
    tracks = get_tracks_by_emotion(emotion, limit=5)

    # Display the recommended tracks
    print(f"Recommended Tracks for {emotion.capitalize()} emotion:")
    for idx, track in enumerate(tracks, 1):
        print(f"{idx}. {track['name']} by {track['artist']} - {track['url']}")

if __name__ == "__main__":
    # Example of recommending music based on an emotion (could be dynamic later)
    emotion = "happy"  # This could come from the emotion detection process
    recommend_music(emotion)
