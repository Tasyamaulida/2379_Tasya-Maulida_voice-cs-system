import os
from pydub import AudioSegment

def preprocess_audio(input_path, output_path):
    """
    Melakukan remux/resampling audio agar kompatibel dengan model STT.
    Mengubah ke: 16kHz, Mono, format WAV.
    """
    try:
        # Load audio (mendukung berbagai format: mp4, m4a, wav, dll)
        audio = AudioSegment.from_file(input_path)
        
        # Resampling ke 16000 Hz dan Mono channel
        audio = audio.set_frame_rate(16000).set_channels(1)
        
        # Simpan hasil
        audio.export(output_path, format="wav")
        print(f"Berhasil remux: {output_path}")
        return True
    except Exception as e:
        print(f"Gagal preprocessing audio: {e}")
        return False