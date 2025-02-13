''' 
Executing this function initiates the application of emotion detection to be executed 
by Flask and deployed on localhost:5000.
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# pylint: disable=W0718

#Initiate the flask app
app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detect():
    ''' 
    This code receives the text from the HTML interface and 
    runs emotion detector over it using the emotion_detector()
    method. The output returned is a dict showing the level of
    each emotion and the dominant emotion of the text..
    '''
    text = request.args.get('textToAnalyze')
    try:
        emotion_dict = emotion_detector(text)
    
        return ("For the given statement, the system response is "
                + f"'anger': {emotion_dict['anger']}, "
                + f"'disgust': {emotion_dict['disgust']}, 'fear': {emotion_dict['fear']}, "
                + f"'joy': {emotion_dict['joy']} and 'sadness': {emotion_dict['sadness']}. "
                + f"The dominant emotion is {emotion_dict['dominant']}.")
    except Exception:
        return "Invalid input! Try again."


@app.route("/")
def render_index_page():
    ''' 
    This function initiates the rendering of the main application
    page over the Flask channel
    '''
    return render_template("index.html")


if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000
    app.run(port=5000, debug=True)
