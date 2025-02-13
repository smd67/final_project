"""
This module contains the function to analyze the sentiment of a given text using the emotion 
detection model.
"""

from typing import List

import requests
from pydantic import BaseModel

# pylint: disable=C0115

# Global Constants
URL = (
    "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/"
    + "NlpService/EmotionPredict"
)
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
INPUT_JSON = {"raw_document": {"text": None}}
TIMEOUT_VALUE = 30


class ProducerId(BaseModel):
    """
    ProducerId model
    """

    name: str
    version: str


class Emotion(BaseModel):
    """
    Emotion model
    """

    anger: float
    disgust: float
    fear: float
    joy: float
    sadness: float


class Span(BaseModel):
    """
    Span model
    """

    begin: int
    end: int
    text: str


class EmotionMentions(BaseModel):
    """
    EmotionMentions model
    """

    span: Span
    emotion: Emotion


class EmotionPredictions(BaseModel):
    """
    EmotionPredictions model
    """

    emotion: Emotion
    target: str
    emotionMentions: List[EmotionMentions]


class Prediction(BaseModel):
    """
    Prediction model
    """

    emotionPredictions: List[EmotionPredictions]
    producerId: ProducerId


def emotion_detector(text_to_analyse: str) -> dict:
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
    prediction = Prediction.model_validate(response.json())
    emotions = prediction.emotionPredictions[0].emotion.model_dump().copy()
    dominant_emotion = max(emotions, key=emotions.get)
    emotions["dominant_emotion"] = dominant_emotion
    return emotions


def emotion_detector_raw(text_to_analyse: str) -> dict:
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
    return response.json()
