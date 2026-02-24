# music-visualizer

Generate video visualizations from music. Analyzes audio to extract bass energy and creates a pulsing visual synced to the beat.

## Installation

Requires Python 3.12+

```bash
git clone https://github.com/yourusername/music-visualizer.git
cd music-visualizer
uv sync
```

## Usage

```bash
uv run python src/main.py <audio_file>
```

Example:

```bash
uv run python src/main.py audio_files/song.flac
```

Output videos are saved to `output/`.

## How it works

1. **Audio analysis** - Uses librosa to extract bass frequencies (<=150Hz) and compute energy over time
2. **Frame generation** - Renders frames with a circle that scales based on bass energy
3. **Video encoding** - Combines frames with the original audio using moviepy
