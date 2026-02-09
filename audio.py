import librosa
import numpy as np


def analyze_audio(file_path, hop_length=512):
    y, sr = load_audio(file_path)
    bass_energy = extract_bass_energy(y, sr, hop_length)
    fps = sr / hop_length
    return bass_energy, fps


def load_audio(file_path):
    y, sr = librosa.load(file_path)
    print(f"Sample rate: {sr}")
    print(f"Duration: {len(y) / sr:.2f} seconds")
    print(f"Samples: {len(y)}")
    return y, sr


def extract_bass_energy(y, sr, hop_length=512):
    stft = librosa.stft(y, hop_length=hop_length)
    magnitudes = np.abs(stft)
    freqs = librosa.fft_frequencies(sr=sr, n_fft=2048)
    bass_mask = freqs <= 150
    bass_energy = magnitudes[bass_mask].mean(axis=0)
    bass_energy = bass_energy / bass_energy.max()
    return bass_energy
