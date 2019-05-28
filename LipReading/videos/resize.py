import moviepy.editor as mp

clip = mp.VideoFileClip("CUSTOMERS.mp4")
clip_resized = clip.resize(height=360) 
clip_resized.write_videofile("rcustomers.mp4")

clip = mp.VideoFileClip("LEGAL.mp4")
clip_resized = clip.resize(height=360) 
clip_resized.write_videofile("rlegal.mp4")

clip = mp.VideoFileClip("REMEMBER.mp4")
clip_resized = clip.resize(height=360) 
clip_resized.write_videofile("rremember.mp4")

clip = mp.VideoFileClip("SOCIETY.mp4")
clip_resized = clip.resize(height=360) 
clip_resized.write_videofile("rsociety.mp4")

clip = mp.VideoFileClip("SUNSHINE.mp4")
clip_resized = clip.resize(height=360) 
clip_resized.write_videofile("rsunshine.mp4")

clip = mp.VideoFileClip("TOMORROW.mp4")
clip_resized = clip.resize(height=360) 
clip_resized.write_videofile("rtomorrow.mp4")

clip = mp.VideoFileClip("VIOLENCE.mp4")
clip_resized = clip.resize(height=360) 
clip_resized.write_videofile("rviolence.mp4")

clip = mp.VideoFileClip("WHETHER.mp4")
clip_resized = clip.resize(height=360) 
clip_resized.write_videofile("rwhether.mp4")

clip = mp.VideoFileClip("YOUNG.mp4")
clip_resized = clip.resize(height=360) 
clip_resized.write_videofile("ryoung.mp4")