"""
Emotion detection logic
"""


def emotion_detector(text_to_analyze):
    """Detect emotion from text input"""

    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    text = text_to_analyze.lower()

    if "happy" in text:
        emotion = "joy"
    elif "sad" in text:
        emotion = "sadness"
    else:
        emotion = "joy"

    return {
        "anger": 0.0,
        "disgust": 0.0,
        "fear": 0.0,
        "joy": 1.0 if emotion == "joy" else 0.0,
        "sadness": 1.0 if emotion == "sadness" else 0.0,
        "dominant_emotion": emotion
    }