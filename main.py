import sys
from audio import load_audio


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <audio_file>")
        sys.exit(1)

    audio_path = sys.argv[1]
    y, sr = load_audio(audio_path)