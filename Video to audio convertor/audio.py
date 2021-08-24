import moviepy.editor as mp
video = mp.VideoFileClip(r"Rock paper scissors.mp4")
video.audio.write_audiofile(r"output.mp3")