# -*- coding: utf-8 -*-

import sys, os
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))
from flowlauncher import FlowLauncher
from pytube import YouTube
from pathlib import Path


class YoutubeDownload(FlowLauncher):
    
    def is_valid_url(self, url):
        try:
            youtube = YouTube(url)
            return True
        except:
            return False


    def query(self, query):
        self.queryd = query

        # Cases:
        # Empty query
        if not query:
            return [
            {
                "Title": "Where's your URL?",
                "SubTitle": "Please, paste a YouTube URL!",
                "IcoPath": "Images/question.png"
            }
        ]
            
        # Invalid URL
        elif not self.is_valid_url(query):
            return [
                {
                    "Title": "Invalid URL!", 
                    "SubTitle": "Please, check if the URL or video is available.",
                    "IcoPath": "Images/stop.png"
                }
            ]

        # Valid URL
        return [
            # Audio option
            {
                "Title": "Download the audio from your video",
                "SubTitle": "Download the audio in .mp3",
                "IcoPath": "Images/audio.png",
                "JsonRPCAction": {
                    "method": "download_audio",
                    "parameters": [query]
                }
            },
            # Video option
            {
                "Title": "Download your video in full quality",
                "SubTitle": "Download the video in .mp4",
                "IcoPath": "Images/video.png",
                "JsonRPCAction": {
                    "method": "download_video",
                    "parameters": [query]
                }
            }
        ]


    def context_menu(self, data):
        return []

    def download_audio(self, url):
        youtube = YouTube(url)
        video = youtube.streams.filter(only_audio = True).first()
        audio_file = video.download(output_path = "Your Downloads")
        base, ext = os.path.splitext(audio_file) # Get the file name
        os.replace(audio_file, base + '.mp3')    # Convert to mp3
        os.system(f'explorer "{os.path.abspath(r".\Your Downloads")}"')

    def download_video(self, url):
        youtube = YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video_file = video.download(output_path = "Your Downloads")
        os.system(f'explorer "{os.path.abspath(r".\Your Downloads")}"')


if __name__ == "__main__":
    YoutubeDownload()
