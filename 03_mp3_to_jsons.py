import whisper
import os
import json

audios = os.listdir("audios")

model = whisper.load_model("base")

for audio in audios:

    result = model.transcribe(f"audios/{audio}",
                              word_timestamps=False)

    chunks = []

    for segment in result["segments"]:
        chunks.append({
            "start": segment["start"],
            "end": segment["end"],
            "text": segment["text"].strip()
        })
    
    final_chunk = {
        "chunks" : chunks,
        "meta_data" : result["text"],
        "video_name" : audio.split(".")[0]
    }
        
    json_name = f"{os.path.splitext(audio)[0]}.json"
        
    with open(f"jsons/{json_name}", "w", encoding="utf-8") as f:
        json.dump(final_chunk, f, indent=4, ensure_ascii=False)

    print(f"Transcribed {audio} and saved to {json_name}")