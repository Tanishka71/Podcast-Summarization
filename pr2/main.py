import json
from yt_extractor import get_audio_url,get_video_infos
from api_communication import save_trascript

def save_video_sentiments(url):
    video_infos=get_video_infos(url)
    audio_url=get_audio_url(video_infos)
    title=video_infos["title"]
    title=title.strip().replace(" ","_")
    title="data/"+title
    save_trascript(audio_url,title,sentiment_analysis=True)

if __name__=="__main__":
    save_video_sentiments("https://www.youtube.com/watch?v=e-kSGNzu0hM")