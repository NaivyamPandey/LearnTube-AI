import requests
import os
import json
import pandas as pd

def create_embedding(text_list):
    r = requests.post(
        "http://localhost:11434/api/embed", json={
            "model" : "bge-m3",
            "input" : text_list
        }
    )
    return r.json()["embeddings"]

def main():

    jsons = os.listdir("jsons")

    list_of_chunks = []
    chunk_id = 0

    for json_file in jsons:
        with open(f"jsons/{json_file}", "r", encoding="utf-8") as f:
            data = json.load(f)
        print(f"Creating embedding for {json_file}")
        
        all_embeddings = []

        texts = [chunk['text'] for chunk in data['chunks']]

        batch_size = 100

        for i in range(0, len(texts), batch_size):
            batch = texts[i:i + batch_size]
            batch_embeddings = create_embedding(batch)
            all_embeddings.extend(batch_embeddings)
            print(f"Batch {i}")

        embeddings = all_embeddings
        video_name = data['video_name']
            
        for i, chunk in enumerate(data['chunks']):
            chunk['chunk_id'] = chunk_id
            chunk['video_name'] = video_name
            chunk['embedding'] = embeddings[i]
            list_of_chunks.append(chunk)
            chunk_id += 1
        
    df = pd.DataFrame.from_records(list_of_chunks)
    df.to_pickle("chunks.pkl")
    
if __name__ == "__main__":
    main()