import requests

with open("prompt.txt", "r") as f:
    prompt = f.read()
    
def inference(prompt):
    r = requests.post("http://localhost:11434/api/generate", json={
        "model" : "llama3.2:3b",
        "prompt" : prompt,
        "stream" : False
    })
    return r.json()['response']

response = inference(prompt)

with open("response.txt", "w") as f:
    f.write(response)