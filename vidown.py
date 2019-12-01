def download(name,link):
    from pytube import YouTube
    YouTube(link).streams.first().download('video/{}'.format(name) ,filename="videostream")
