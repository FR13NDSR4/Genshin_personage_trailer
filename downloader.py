from pytube import YouTube


def video_downloader(video_url, filename):
    my_video = YouTube(video_url)
    YouTube(video_url).streams.filter(res="720p").first().download(filename=filename + ".mp4")
    return my_video.title
