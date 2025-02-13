'''
This file contains the test cases for the emotion detection function.
'''
import json as js
from unittest.mock import MagicMock, patch
from EmotionDetection.emotion_detection import emotion_detector

# pylint: disable=W0613, W0718
@patch("requests.post")
def test_emotion_detection(mock_post):
    """
    Test the emotion detection function.
    """

    def mock_post_func(url, json, headers, timeout=10):
        """
        Mock post function.
        """
        with open("tests/output.json", encoding='utf-8') as f:
            json_data = js.load(f)
        retval = MagicMock()
        retval.json.return_value = json_data
        retval.text = str(json_data)
        retval.status_code = 200
        return retval

    mock_post.side_effect = mock_post_func
    emotion_dict = emotion_detector("I love this new technology.")
    assert emotion_dict['anger'] == 0.01364663
    assert emotion_dict['disgust'] == 0.0017160787
    assert emotion_dict['fear'] == 0.008986978
    assert emotion_dict['joy'] == 0.9719017
    assert emotion_dict['sadness'] == 0.055187024
    assert emotion_dict['dominant_emotion'] == 'joy'

@patch("requests.post")
def test_emotion_detection_joy(mock_post):
    """
    Test the emotion detection function with an input that should return joy.
    """
    def mock_post_func(url, json, headers, timeout=10):
        """
        Mock post function.
        """
        with open("tests/output_joy.json", encoding='utf-8') as f:
            json_data = js.load(f)
        retval = MagicMock()
        retval.json.return_value = json_data
        retval.text = str(json_data)
        retval.status_code = 200
        return retval

    mock_post.side_effect = mock_post_func
    emotion_dict = emotion_detector("I am glad this happened")
    assert emotion_dict['dominant_emotion'] == 'joy'

@patch("requests.post")
def test_emotion_detection_sadness(mock_post):
    """
    Test the emotion detection function with an input that should return sadness.
    """
    def mock_post_func(url, json, headers, timeout=10):
        """
        Mock post function.
        """
        with open("tests/output_sad.json", encoding='utf-8') as f:
            json_data = js.load(f)
        retval = MagicMock()
        retval.json.return_value = json_data
        retval.text = str(json_data)
        retval.status_code = 200
        return retval

    mock_post.side_effect = mock_post_func
    emotion_dict = emotion_detector("I am so sad about this")
    assert emotion_dict['dominant_emotion'] == 'sadness'

@patch("requests.post")
def test_emotion_detection_anger(mock_post):
    """
    Test the emotion detection function with an input that should return anger.
    """
    def mock_post_func(url, json, headers, timeout=10):
        """
        Mock post function.
        """
        with open("tests/output_anger.json", encoding='utf-8') as f:
            json_data = js.load(f)
        retval = MagicMock()
        retval.json.return_value = json_data
        retval.text = str(json_data)
        retval.status_code = 200
        return retval

    mock_post.side_effect = mock_post_func
    emotion_dict = emotion_detector("I am really mad about this")
    assert emotion_dict['dominant_emotion'] == 'anger'

@patch("requests.post")
def test_emotion_detection_fear(mock_post):
    """
    Test the emotion detection function with an input that should return fear.
    """
    def mock_post_func(url, json, headers, timeout=10):
        """
        Mock post function.
        """
        with open("tests/output_fear.json", encoding='utf-8') as f:
            json_data = js.load(f)
        retval = MagicMock()
        retval.json.return_value = json_data
        retval.text = str(json_data)
        retval.status_code = 200
        return retval

    mock_post.side_effect = mock_post_func
    emotion_dict = emotion_detector("I am really afraid that this will happen")
    assert emotion_dict['dominant_emotion'] == 'fear'

@patch("requests.post")
def test_emotion_detection_disgust(mock_post):
    """
    Test the emotion detection function with an input that should return disgust.
    """
    def mock_post_func(url, json, headers, timeout=10):
        """
        Mock post function.
        """
        with open("tests/output_disgusted.json", encoding='utf-8') as f:
            json_data = js.load(f)
        retval = MagicMock()
        retval.json.return_value = json_data
        retval.text = str(json_data)
        retval.status_code = 200
        return retval

    mock_post.side_effect = mock_post_func
    emotion_dict = emotion_detector("I feel disgusted just hearing about this")
    assert emotion_dict['dominant_emotion'] == 'disgust'
