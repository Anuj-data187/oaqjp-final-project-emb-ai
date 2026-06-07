# 5a_unit_testing
import unittest
from emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_joy(self):
        result = emotion_detector('I am very happy')
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_sadness(self):
        result = emotion_detector('I am very sad')
        self.assertEqual(result['dominant_emotion'], 'sadness') # Adjust mock data as needed

    def test_empty_input(self):
        result = emotion_detector('')
        self.assertIsNone(result['dominant_emotion'])

if __name__ == '__main__':
    unittest.main()