from pytube import YouTube
video = YouTube('https://www.youtube.com/watch?v=PxrnoGyBw4E')
video.streams.all()
stream = video.streams.all()
for i in stream:
  print(i)
