import yt_dlp
import os

os.makedirs("videos_webm", exist_ok=True)

playlist_url = "https://www.youtube.com/watch?v=iPGXk-i-VYU&list=PLRAV69dS1uWR7KF-zV6YPYtKYEHENETyE"

ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": "videos/%(title)s.%(ext)s"
}
    
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])