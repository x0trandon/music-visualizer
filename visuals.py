from PIL import Image, ImageDraw


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