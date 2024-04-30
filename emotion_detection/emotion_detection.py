""" 
Module that executes a emotion detection
from any text, and return a result based 
of type of the emotion.
"""
import json
import requests


def emotion_detector(text_to_analyze): # POST request
    """
    send a POST request to the relevant model 
    with the required text and the model will send the appropriate response
    """
    url = ('https://sn-watson-emotion.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/EmotionPredict')
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_object = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, timeout=10, json=json_object, headers=header)
    response_dict = json.loads(response.text)  # convert text into a dictionary

    if response.status_code == 200:
        # Extract the required set of emotions and their scores
        anger_score = response_dict["emotionPredictions"][0]["emotion"]["anger"]
        disgust_score = response_dict["emotionPredictions"][0]["emotion"]["disgust"]
        fear_score = response_dict["emotionPredictions"][0]["emotion"]["fear"]
        joy_score = response_dict["emotionPredictions"][0]["emotion"]["joy"]
        sadness_score = response_dict["emotionPredictions"][0]["emotion"]["sadness"]

        # Find the dominant emotion
        emotions = [anger_score, disgust_score,
                    fear_score, joy_score, sadness_score]
        dominant_emotion_i = emotions.index(max(emotions))
        emotion_keys = ["anger", "disgust", "fear", "joy", "sadness"]
        dominant_emotion_key = emotion_keys[dominant_emotion_i]

    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion_key = None

    # Return the output
    output = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion_key
    }
    return output
