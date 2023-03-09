# -*- coding: utf-8 -*-

import sys,os
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from flowlauncher import FlowLauncher
import pytube
from pathlib import Path
from time import sleep
import ctypes
from random import randint
class YoutubeDownload(FlowLauncher):

    def query(self, query):
        if not query.startswith("https://www.youtube.com") or query.startswith("https://youtu.be"):
            return
        self.queryd = query
        try:
            yt_vid = pytube.YouTube(query)
        except:
            return [{
                "Title": "Invalid link!",
                "SubTitle": "Please enter a valid youtube link!",
                "IcoPath": "cat.png",
                "JsonRPCAction": {
                    "method": "",
                    "parameters": []
                }}]
        
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
        yt_video = pytube.YouTube(url)
        mp3 = yt_video.streams.filter(only_audio=True).first()
        home = str(Path.home())
        os.chdir("{}\\Downloads".format(home))
        out_audio = mp3.download()
        MessageBox = ctypes.windll.user32.MessageBoxW
        MessageBox(None, 'Your Video Is Downloading...', 'Message', 0)
        base, ext = os.path.splitext(out_audio)
        new_file = base + '.mp3'
        if os.path.isfile(new_file):
            new_file = base+str(randint(1,100000)) + '.mp3'
            os.rename(out_audio, new_file)
            os.system("explorer .")
            return
        os.rename(out_audio, new_file)
        os.system("explorer .")


    def download_video(self, url):
        yt_video = pytube.YouTube(url)
        mp4 = yt_video.streams.get_highest_resolution()
        home = str(Path.home())
        os.chdir("{}\\Downloads".format(home))
        out_video = mp4.download()
        MessageBox = ctypes.windll.user32.MessageBoxW
        MessageBox(None, 'Your Video Is Downloading...', 'Message', 0)
        base, ext = os.path.splitext(out_video)
        new_file = base + '.mp4'
        if os.path.isfile(new_file):
            new_file = base+str(randint(1,100000)) + '.mp4'
            os.rename(out_video, new_file)
            os.system("explorer .")
            return
        os.rename(out_video, new_file)

        os.system("explorer .")

if __name__ == "__main__":
    YoutubeDownload()

