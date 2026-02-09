import librosa

def load_audio(file_path):
    y, sr = librosa.load(file_path)
    print(f"Sample rate: {sr}")
    print(f"Duration: {len(y) / sr:.2f} seconds")
    print(f"Samples: {len(y)}")
    return y, sr