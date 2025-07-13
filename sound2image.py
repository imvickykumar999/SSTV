from pydub import AudioSegment
import os
import subprocess

# Input paths
mp3_path = "sound/wall.mp3"
wav_path = "sound/wall.wav"
output_image = "decoded_image.png"

# Convert MP3 to WAV (44100 Hz)
audio = AudioSegment.from_mp3(mp3_path).set_frame_rate(44100).set_channels(1)
audio.export(wav_path, format="wav")

# Run rxsstv on WAV file
# Make sure rxsstv is installed and in PATH
# rxsstv only accepts stdin or wav as file
try:
    subprocess.run([
        "rxsstv",
        "-o", output_image,
        wav_path
    ], check=True)
    print(f"✅ Image decoded and saved to: {output_image}")
except subprocess.CalledProcessError as e:
    print("❌ Failed to decode SSTV:", e)
