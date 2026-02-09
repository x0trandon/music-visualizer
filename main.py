import sys
import os
from audio import load_audio, extract_bass_energy
from visuals import generate_frames
from video import encode_video


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <audio_file>")
        sys.exit(1)

    audio_path = sys.argv[1]
    y, sr = load_audio(audio_path)

    hop_length = 512
    fps = sr / hop_length

    bass_energy = extract_bass_energy(y, sr, hop_length=hop_length)

    audio_name = os.path.splitext(os.path.basename(audio_path))[0]
    output_path = f"output/{audio_name}_video.mp4"

    print(f"Generating {len(bass_energy)} frames at {fps:.1f} fps...")
    frames = generate_frames(bass_energy)

    print("Encoding video...")
    encode_video(frames, fps, audio_path, output_path)

    print(f"Done! Output saved to {output_path}")