import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobject = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = myobject, headers = header)
    formatted_response = response.json()

    emotions = {
    'anger': 0,
    'disgust': 0,
    'fear': 0,
    'joy': 0,
    'sadness': 0,
    'dominant_emotion': 'name'
    }

    if response.status_code == 400:
        for emotion in emotions:
            emotions[emotion] = None
    else:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
    
        dominant_emotion = max(emotions.items(), key=lambda k: k[1])[0]
        emotions['dominant_emotion'] = dominant_emotion 
    

    return emotions