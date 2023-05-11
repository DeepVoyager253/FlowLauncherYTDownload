# -*- coding: utf-8 -*-

import sys,os
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from flowlauncher import FlowLauncher
import os
from pytube import YouTube
from pathlib import Path
class YoutubeDownload(FlowLauncher):

    def query(self, query):
        # if not query.startswith("https://www.youtube.com") and not query.startswith("https://youtu.be"):
        #     return [            {
        #         "Title": "Invalid URL!",
        #         "SubTitle": "This is an Invalid youtube URL!",
        #         "IcoPath": "Images/Media_Player_Windows_11_logo.png"
        #     }]
        self.queryd = query
        return [
            {
                "Title": "Download your video's audio.",
                "SubTitle": "Download 's audio into an mp3.",
                "IcoPath": "Images/Media_Player_Windows_11_logo.png",
                "JsonRPCAction": {
                    "method": "download_audio",
                    "parameters": []
                }
            },
                {
                "Title": "Download your video in full quality.",
                "SubTitle": "Download 's video into an mp4.",
                "IcoPath": "Images/7-player_windows_media_player_video-512.png",
                "JsonRPCAction": {
                    "method": "download_video",
                    "parameters": []
                }
            }
        ]

    def context_menu(self, data):
        return []



    def download_audio(self):
        os.chdir("%USERPROFILE%")
        url = self.queryd
        try:
            youtube = YouTube(url)
            video = youtube.streams.filter(only_audio=True).first()
            output_path = os.path.join(os.getcwd(), "downloads")
            os.makedirs(output_path, exist_ok=True)
            audio_file = video.download(output_path=output_path)
            print("Audio downloaded successfully!")
            print("File saved at:", audio_file)
            os.system("explorer .")
        except Exception as e:
            print("Error:", str(e))

    def download_video(self):
        os.chdir("%USERPROFILE%")
        url = self.queryd
        try:
            youtube = YouTube(url)
            video = youtube.streams.filter(progressive=True, file_extension='mp4').first()
            video_file = video.download()
            print("Video downloaded successfully!")
            print("File saved at:", video_file)
            os.system("explorer .")
        except Exception as e:
            print("Error:", str(e))

if __name__ == "__main__":
    YoutubeDownload()

