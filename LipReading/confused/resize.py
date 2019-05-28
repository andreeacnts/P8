import moviepy.editor as mp

clip = mp.VideoFileClip("BORDER.mp4")
clip_resized = clip.resize(height=360) 
clip_resized.write_videofile("rborder.mp4")

clip = mp.VideoFileClip("CAPITAL.mp4")
clip_resized = clip.resize(height=360) 
clip_resized.write_videofile("rcapital.mp4")

clip = mp.VideoFileClip("CLAIMS.mp4")
clip_resized = clip.resize(height=360) 
clip_resized.write_videofile("rclaims.mp4")

clip = mp.VideoFileClip("GAMES.mp4")
clip_resized = clip.resize(height=360) 
clip_resized.write_videofile("rgames.mp4")

clip = mp.VideoFileClip("HAPPEN.mp4")
clip_resized = clip.resize(height=360) 
clip_resized.write_videofile("rhappen.mp4")

clip = mp.VideoFileClip("IMPORTANT.mp4")
clip_resized = clip.resize(height=360) 
clip_resized.write_videofile("rimportant.mp4")

clip = mp.VideoFileClip("MORNING.mp4")
clip_resized = clip.resize(height=360) 
clip_resized.write_videofile("rmorning.mp4")

clip = mp.VideoFileClip("SEVEN.mp4")
clip_resized = clip.resize(height=360) 
clip_resized.write_videofile("rseven.mp4")

clip = mp.VideoFileClip("SEVERAL.mp4")
clip_resized = clip.resize(height=360) 
clip_resized.write_videofile("rseveral.mp4")

clip = mp.VideoFileClip("WARNING.mp4")
clip_resized = clip.resize(height=360) 
clip_resized.write_videofile("rwarning.mp4")