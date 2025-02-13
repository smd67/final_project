""" 
Executing this function initiates the application of emotion detection to be executed 
by Flask and deployed on localhost:5000.
"""

from flask import Flask, render_template, request
from requests.exceptions import HTTPError

from EmotionDetection.emotion_detection import emotion_detector

# pylint: disable=W0718

# Initiate the flask app
app = Flask(__name__)


def format_output(emotion_dict: dict) -> str:
    """
    This function formats the output of the emotion detection
    function into a readable format.
    """
    retval = (
        "For the given statement, the system response is "
        + f"'anger': {emotion_dict.get('anger', None)}, "
        + f"'disgust': {emotion_dict.get('disgust', None)}, "
        + f"'fear': {emotion_dict.get('fear', None)}, "
        + f"'joy': {emotion_dict.get('joy', None)} and "
        + f"'sadness': {emotion_dict.get('sadness', None)}. "
        + f"The dominant emotion is {emotion_dict.get('dominant_emotion', None)}."
    )
    # Return "Invalid input! Try again." if emotion_dict['dominant_emotion'] is None.
    return (
        retval
        if emotion_dict.get("dominant_emotion", None)
        else "Invalid input! Try again."
    )


@app.route("/emotionDetector")
def emotion_detect():
    """
    This code receives the text from the HTML interface and
    runs emotion detector over it using the emotion_detector()
    method. The output returned is a dict showing the level of
    each emotion and the dominant emotion of the text..
    """
    text = request.args.get("textToAnalyze")
    emotion_dict = {}
    try:
        emotion_dict = emotion_detector(text)
        return format_output(emotion_dict)
    except HTTPError as e:
        if e.response.status_code == 400:
            return format_output(emotion_dict)
        return "Invalid input! Try again."
    except Exception:
        return "Invalid input! Try again."


@app.route("/")
def render_index_page():
    """
    This function initiates the rendering of the main application
    page over the Flask channel
    """
    return render_template("index.html")


if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000
    app.run(port=5000, debug=True)
