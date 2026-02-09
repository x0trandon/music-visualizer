from PIL import Image, ImageDraw
import numpy as np


def render_frame(energy, width=1920, height=1080):
    img = Image.new("RGB", (width, height), (0, 0, 0))
    draw = ImageDraw.Draw(img)

    center_x = width // 2
    center_y = height // 2

    min_radius = 50
    max_radius = 300
    radius = min_radius + energy * (max_radius - min_radius)

    draw.ellipse(
        [
            center_x - radius,
            center_y - radius,
            center_x + radius,
            center_y + radius,
        ],
        fill=(255, 255, 255),
    )

    return img


def generate_frames(bass_energy):
    frames = []
    for i, energy in enumerate(bass_energy):
        img = render_frame(energy)
        frames.append(np.array(img))

        if (i + 1) % 100 == 0:
            print(f"Rendered frame {i + 1}/{len(bass_energy)}")

    return frames