import requests

API_URL = "http://localhost:3000/api/v1/prediction/a376ee8b-2d5b-4482-a74a-41bc3d176518"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()
    
output = query({
    "question": "Hey, how are you?",
})
