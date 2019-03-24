from pytube import YouTube
video = YouTube('https://www.youtube.com/watch?v=d3D7Y_ycSms')
print(video.title)
print(video.video_id)
print(video.age_restricted)
