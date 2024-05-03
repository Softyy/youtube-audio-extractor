import os
import yt_dlp
from youtube_audio.app import app

@app.command()
def extract(youtube_url: str, output_folder: str = "./files", temp_folder: str = ""):
    # make output folder in case it doesn't exist
    os.makedirs(os.path.dirname(output_folder), exist_ok=True)
    ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl':'%(title)s',     # name the file the ID of the video
            'embedthumbnail': True,
            'paths': {
                "home": output_folder,
                "temp": temp_folder,
            },
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }, {
                'key': 'FFmpegMetadata',
            }]
        }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        _info_dict = ydl.extract_info(youtube_url, download=True)
