from pytube import YouTube
from os import *
from pathlib import Path
from pywebio.input import *
from pywebio.output import *

#C:\Users\logonucd\Downloads\ze_da_manga

def baixar_video():
    yt = YouTube
    while True:
        link_video = input("digite o link do video a ser baixado...")
        if link_video.split('//')[0] == "https:":
            put_text("em andamento...".title()).style("color: red; 75px")
            url_do_video = yt(link_video)
            viedo = url_do_video.streams.get_highest_resolution()
            # voce coloca o path do seu sistema, esse é o meu sistema nao vai funcionar com você
            Path_to_download = (r'C:\Users\logonucd\Downloads\ze_da_manga')
            viedo.download(Path_to_download)
            # voce coloca o path do seu sistema, esse é o meu sistema nao vai funcionar com você
            put_text('download concluido'.title()).style("color: red; 75px")
            startfile(r'C:\\Users\\logonucd\\Downloads\\ze_da_manga')
            
            
            
            
            
            
if __name__ in "__main__":
    baixar_video()