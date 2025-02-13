"""
This module contains the function to analyze the sentiment of a given text using the emotion 
detection model.
"""

import requests

# Global Constants
URL = (
    "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/"
    + "NlpService/EmotionPredict"
)
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
INPUT_JSON = {"raw_document": {"text": None}}
TIMEOUT_VALUE = 30


def emotion_detector(text_to_analyse: str) -> str:
    """
    Analyze the sentiment of the given text using the emotion detection model.
    """
    print(f"Analyzing emotion: {text_to_analyse}")
    url = URL
    headers = HEADERS

    # deep copy of the json object INPUT_JSON
    myobj = INPUT_JSON.copy()
    myobj["raw_document"]["text"] = text_to_analyse

    response = requests.post(url, json=myobj, headers=headers, timeout=TIMEOUT_VALUE)
    response.raise_for_status()
    return response.text
