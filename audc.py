def audc(name):
    import sys
    from moviepy.editor import VideoFileClip
    video = VideoFileClip('video/{}/videostream.mp4'.format(name))
    audio = video.audio # 3.
    audio.write_audiofile("ul/{}/audio.wav".format(name)) # 4.

