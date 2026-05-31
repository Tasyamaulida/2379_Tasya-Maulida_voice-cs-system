import csv
import os

from app.tts import text_to_speech

INPUT_FILE = "results_llm.csv"
OUTPUT_DIR = "data/audio_ai"

os.makedirs(
    OUTPUT_DIR,
    exist_ok=True
)

with open(
    INPUT_FILE,
    "r",
    encoding="utf-8"
) as f:

    reader = csv.reader(f)

    next(reader, None)

    for index, row in enumerate(reader, start=1):

        if len(row) < 2:
            continue

        response = row[1]

        if (
            not response
            or response == "ERROR_QUOTA"
            or response == "ERROR_GEMINI"
        ):
            continue

        output_wav = os.path.join(
            OUTPUT_DIR,
            f"response_{index}.wav"
        )

        if os.path.exists(output_wav):
            continue

        print("=" * 50)
        print(f"Membuat audio {index}")

        success = text_to_speech(
            response,
            output_wav
        )

        if success:
            print(f"Berhasil: {output_wav}")
        else:
            print(f"Gagal: {output_wav}")

print("\nSELESAI MEMBUAT AUDIO")