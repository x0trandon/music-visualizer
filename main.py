import sys
from audio import load_audio


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <audio_file>")
        sys.exit(1)

    audio_path = sys.argv[1]
    y, sr = load_audio(audio_path)

    bass_energy = extract_bass_energy(y, sr)
    print(f"Bass energy frames: {len(bass_energy)}")
    print(f"First 10 values: {bass_energy[:10]}")