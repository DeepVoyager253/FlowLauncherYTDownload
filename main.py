# -*- coding: utf-8 -*-

import sys,os
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from flowlauncher import FlowLauncher
import yt_dlp
from pathlib import Path
class YoutubeDownload(FlowLauncher):

    def query(self, query):
        if not query.startswith("https://www.youtube.com") or query.startswith("https://youtu.be"):
            return
        self.queryd = query
        return [
            {
                "Title": "Download your video's audio.",
                "SubTitle": "Download 's audio into an mp3.",
                "IcoPath": "Images/Media_Player_Windows_11_logo.png",
                "JsonRPCAction": {
                    "method": "download_audio",
                    "parameters": ["{}".format(query)]
                }
            },
                {
                "Title": "Download your video in full quality.",
                "SubTitle": "Download 's video into an mp4.",
                "IcoPath": "Images/7-player_windows_media_player_video-512.png",
                "JsonRPCAction": {
                    "method": "download_video",
                    "parameters": ["{}".format(query)]
                }
            }
        ]

    def context_menu(self, data):
        return []


    def download_audio(self, url):
        os.chdir(str(Path.home() / "Downloads"))
        
        ydl_opts = {
            'format': 'm4a/bestaudio/best',
            # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
            'postprocessors': [{  # Extract audio using ffmpeg
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'm4a',
            }]
        }
            
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        os.system("explorer .")


    def download_video(self, url):
        os.chdir(str(Path.home() / "Downloads"))
        
        ydl_opts = {
            'format': 'mp4',
            }
            
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        os.system("explorer .")
if __name__ == "__main__":
    YoutubeDownload()

