from PIL import Image
from pysstv.color import Robot36
from pydub import AudioSegment
import io
import os

# Ask user for image filename (e.g., wall.png)
image_filename = input("Enter the image filename with extension (e.g., wall.png): ")

# Construct full paths
image_dir = "image"
sound_dir = "sound"
image_path = os.path.join(image_dir, image_filename)
image_name = os.path.splitext(image_filename)[0]  # "wall"

# Ensure sound directory exists
os.makedirs(sound_dir, exist_ok=True)

# Load and resize image
image = Image.open(image_path).resize((320, 240))

# Encode to SSTV (Robot36 mode)
sstv = Robot36(image, 44100, 16)
wav_io = io.BytesIO()
sstv.write_wav(wav_io)
wav_io.seek(0)

# Save as WAV
wav_path = os.path.join(sound_dir, f"{image_name}.wav")
with open(wav_path, "wb") as f:
    f.write(wav_io.read())

# Convert to MP3
wav_io.seek(0)
audio = AudioSegment.from_file(wav_io, format="wav")
mp3_path = os.path.join(sound_dir, f"{image_name}.mp3")
audio.export(mp3_path, format="mp3")

print(f"✅ SSTV audio saved as:\n- WAV: {wav_path}\n- MP3: {mp3_path}")
