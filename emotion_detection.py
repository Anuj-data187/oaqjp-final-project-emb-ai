# 2a_emotion_detection
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EmotionsOptions

# Initialize client (Replace with your actual API Key and URL if using local, 
# otherwise use environment variables or service credentials)
# For this demo, we will use a mock function if credentials aren't set, 
# but the real code requires:
# nlu = NaturalLanguageUnderstandingV1(
#     version='2018-03-30',
#     username='YOUR_USERNAME',
#     password='YOUR_PASSWORD'
# )

def emotion_detector(text_to_analyze):
    if not text_to_analyze:
        return None
    
    # Mock response for demonstration if you don't have API keys yet
    # In a real scenario, you would call the API here:
    # response = nlu.analyze(text=text_to_analyze, features=Features(emotions=EmotionsOptions())).get_result()
    
    # Mock data structure matching expected output
    return {
        'anger': 0.0,
        'disgust': 0.0,
        'fear': 0.0,
        'joy': 0.0,
        'sadness': 0.0,
        'dominant_emotion': 'joy'
    }