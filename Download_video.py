import pytube
video_url = 'https://www.youtube.com/watch?v=tXOIvjbNhts' # copy and paste url
youtube = pytube.YouTube(video_url)
video = youtube.streams.first()
video.download('/home/jay/Downloads') # path, where to video download.
# it may take some tome to download.
