import os
from TTS.api import TTS

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_PATH, "coqui_tts")

MODEL_FILE = os.path.join(
    MODEL_DIR,
    "checkpoint_1260000-inference.pth"
)

CONFIG_FILE = os.path.join(
    MODEL_DIR,
    "config.json"
)

SPEAKER_FILE = os.path.join(
    MODEL_DIR,
    "speakers.pth"
)

print("INFO: Menginisialisasi Model TTS Lokal...")

try:

    tts_engine = TTS(
        model_path=MODEL_FILE,
        config_path=CONFIG_FILE,
        gpu=False
    )

    print("INFO: Model TTS Lokal Berhasil Dimuat!")

    try:

        print("Daftar Speaker:")
        print(tts_engine.speakers)

    except:
        pass

except Exception as e:

    print(
        f"ERROR: Gagal muat model. Detail: {e}"
    )

    tts_engine = None


def text_to_speech(
    text,
    output_wav_path
):

    if tts_engine is None:

        print(
            "DEBUG: TTS Engine tidak aktif."
        )

        return False

    try:

        speaker_name = None

        try:

            if (
                hasattr(tts_engine, "speakers")
                and tts_engine.speakers
            ):

                speaker_name = (
                    tts_engine.speakers[0]
                )

        except:
            pass

        if speaker_name:

            tts_engine.tts_to_file(
                text=text,
                file_path=output_wav_path,
                speaker=speaker_name
            )

        else:

            tts_engine.tts_to_file(
                text=text,
                file_path=output_wav_path
            )

        print(
            f"DEBUG: Berhasil membuat suara: {output_wav_path}"
        )

        return True

    except Exception as e:

        print(
            f"ERROR proses TTS: {e}"
        )

        return False