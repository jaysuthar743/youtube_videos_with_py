import pytube
video_url = 'https://www.youtube.com/watch?v=tXOIvjbNhts' // paste here your Youube videos' url
youtube = pytube.YouTube(video_url)
video = youtube.streams.first()
video.download('/home/jay/Downloads') // path, where to video download.
