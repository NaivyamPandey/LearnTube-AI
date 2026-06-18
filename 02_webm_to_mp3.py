import os
import subprocess

files = os.listdir("videos")
for file in files:
    file_name = file.split(".")[0]
    subprocess.run(["ffmpeg", "-i", f"videos/{file}", f"audios_mp3/{file_name}.mp3"])