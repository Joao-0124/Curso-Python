from youtube_dl import YoutubeDL
import sys
import time

def baixar_info_video(video_id):
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    youtube_dl_options = {}
    with YoutubeDL(youtube_dl_options) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        return info_dict

if __name__ == "__main__":
    video1 = "uhG8UcjsKuo"
    info = baixar_info_video(video1)
    print(info['title'])