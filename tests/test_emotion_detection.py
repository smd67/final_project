'''
This file contains the test cases for the emotion detection function.
'''
import json as js
from unittest.mock import MagicMock, patch
from emotion_detection import emotion_detector

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
