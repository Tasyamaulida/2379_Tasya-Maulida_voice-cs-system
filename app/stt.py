import whisper
import os

# Load model Whisper
model = whisper.load_model("small")

def transcribe_speech(audio_path):
    """
    Mengubah audio menjadi teks menggunakan Whisper
    dengan auto language detection.
    """

    if not os.path.exists(audio_path):
        return "File audio tidak ditemukan."

    try:
        result = model.transcribe(
            audio_path,
            fp16=False  # lebih aman untuk CPU Windows
        )

        text = result["text"].strip()

        detected_lang = result.get("language", "unknown")

        print(f"Bahasa terdeteksi: {detected_lang}")

        return text

    except Exception as e:
        return f"Error STT: {str(e)}"


# Untuk testing langsung
if __name__ == "__main__":

    sample_audio = "data/audio/test.wav"

    if os.path.exists(sample_audio):
        hasil = transcribe_speech(sample_audio)

        print("\n=== HASIL TRANSKRIPSI ===")
        print(hasil)
    else:
        print("File test.wav tidak ditemukan.")