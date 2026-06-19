import os
import json
import math

json_files = os.listdir("jsons")

n = 10

for file in json_files:
    with open(f"jsons/{file}", "r", encoding="utf-8") as f:
        data = json.load(f)
    new_chunks = []
    num_chunks = len(data['chunks'])
    num_groups = math.ceil(num_chunks / n)
    
    for i in range(num_groups):
        start_idx = i*n
        end_idx = min(((i+1)*n), num_chunks)
        
        chunk_group = data['chunks'][start_idx : end_idx]
        
        new_chunks.append({
            "start" : chunk_group[0]["start"],
            "end" : chunk_group[-1]["end"],
            "text" : " ".join(c["text"] for c in chunk_group)
        })
        
    os.makedirs("new_jsons", exist_ok=True)
    with open(os.path.join("new_jsons", file), "w", encoding="utf-8") as f:
        json.dump({
            "chunks" : new_chunks,
            "video_name" : data["video_name"],
            "meta_data" : data["meta_data"]
        }, f, indent=4)
        