import os
from moviepy import ImageSequenceClip


def encode_video(frames, fps, audio_path, output_path="output/output.mp4"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    clip = ImageSequenceClip(frames, fps=fps)
    clip.write_videofile(output_path, audio=audio_path)