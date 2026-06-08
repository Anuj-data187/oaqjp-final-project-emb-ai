"""
Flask server for Emotion Detection application
"""

from flask import Flask, request
from emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    """Home route"""
    return "Emotion Detection App is running!"


@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """Detect emotion from input text"""

    text = request.args.get("textToAnalyze")

    if not text or text.strip() == "":
        return "Invalid input! Please enter text."

    result = emotion_detector(text)

    return (
        f"anger: {result['anger']}, "
        f"disgust: {result['disgust']}, "
        f"fear: {result['fear']}, "
        f"joy: {result['joy']}, "
        f"sadness: {result['sadness']}, "
        f"dominant_emotion: {result['dominant_emotion']}"
    )


if __name__ == "__main__":
    app.run(debug=False)