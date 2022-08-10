from pytube import YouTube
from sys import argv

#pass video link as the parameter
link = argv[1]
video = YouTube(link)

#just for the thrills
print("Title: ", video.title)
print("Views: ", video.views)

#for slow internet speeds
potato_internet = video.streams.filter(res='480p')

#file path to save your videos
potato_internet.download('/path/for/your/downloads')