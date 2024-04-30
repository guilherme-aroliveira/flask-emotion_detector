"""
Executes the necessary tests
"""
import unittest
from emotion_detection.emotion_detection import emotion_detector

class TestEmtionDetector(unittest.TestCase):
    """
    Class that executes the test_function
    """

    def test_emotion_detector(self):
        """
        Function that executes a series of unit tests for
        each the user input and it's related emotion
        """
        test_1 = emotion_detector("I am glad this happened")
        self.assertEqual(test_1['dominant_emotion'], "joy") # unit tests
        test_1 = emotion_detector("I am really mad about this")
        self.assertEqual(test_1['dominant_emotion'], "anger")
        test_1 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(test_1['dominant_emotion'], "disgust")
        test_1 = emotion_detector("I am so sad about this")
        self.assertEqual(test_1['dominant_emotion'], "sadness")
        test_1 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(test_1['dominant_emotion'], "fear")

unittest.main() # call the unit tests
