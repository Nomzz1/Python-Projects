from pytube import YouTube
import os
songList = ["https://www.youtube.com/watch?v=iIWoYaJRryw"]
for i in songList:
    yt = YouTube(i)
    video = yt.streams.filter(only_audio=True, file_extension="mp4",abr="128kbps").first()
    video.download(output_path="C:\\Users\\brain\\Downloads")
    print(yt.title + " has been successfully downloaded.")
