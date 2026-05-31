import os
import csv
from app.stt import transcribe_speech

# Folder audio
audio_dir = "data/audio"

# Cek folder
if not os.path.exists(audio_dir):
    print(f"Folder tidak ditemukan: {audio_dir}")
    exit()

# Ambil semua file wav
audio_files = [
    f for f in os.listdir(audio_dir)
    if f.endswith(".wav")
]

# Untuk testing dulu 10 audio pertama
# audio_files = audio_files[:10]

# untuk semua audio
audio_files = [
    f for f in os.listdir(audio_dir)
    if f.endswith(".wav")
]

print(f"Jumlah audio ditemukan: {len(audio_files)}")

# Buat file CSV
with open(
    "results.csv",
    "w",
    newline="",
    encoding="utf-8"
) as csvfile:

    writer = csv.writer(csvfile)

    # Header CSV
    writer.writerow([
        "audio_file",
        "transcript"
    ])

    # Proses audio satu per satu
    for file in audio_files:

        audio_path = os.path.join(audio_dir, file)

        print("\n" + "=" * 50)
        print(f"Memproses: {file}")

        try:
            text = transcribe_speech(audio_path)

            print("Hasil Transkripsi:")
            print(text)

            # Simpan ke CSV
            writer.writerow([
                file,
                text
            ])

        except Exception as e:
            print(f"Error: {e}")

print("\nSelesai!")
print("Hasil tersimpan di results.csv")