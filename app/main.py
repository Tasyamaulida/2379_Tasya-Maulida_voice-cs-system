from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import os
import uuid
import transformers.pytorch_utils

# Patch Fix Coqui
if not hasattr(transformers.pytorch_utils, "isin_mps_friendly"):
    transformers.pytorch_utils.isin_mps_friendly = lambda x, y: x.isin(y)

from app.stt import transcribe_speech
from app.llm import get_chatbot_response
from app.tts import text_to_speech
from app.utils import preprocess_audio

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

os.makedirs("data/audio", exist_ok=True)

@app.get("/")
def root():
    return {
        "message": "Speech-to-Speech API Running"
    }

@app.post("/voice-chat")
async def voice_chat(audio: UploadFile = File(...)):

    session_id = str(uuid.uuid4())

    raw_path = f"data/audio/{session_id}_raw.wav"
    clean_path = f"data/audio/{session_id}_clean.wav"
    output_audio = f"data/audio/{session_id}_response.wav"

    try:

        # Simpan audio upload
        with open(raw_path, "wb") as f:
            f.write(await audio.read())

        # Preprocess audio
        preprocess_audio(
            raw_path,
            clean_path
        )

        # STT
        user_text = transcribe_speech(
            clean_path
        )

        print("=" * 50)
        print("TRANSCRIPT:")
        print(user_text)

        # LLM
        ai_text = get_chatbot_response(
            user_text
        )

        print("\nLLM RESPONSE:")
        print(ai_text)

        # TTS
        success = text_to_speech(
            ai_text,
            output_audio
        )

        if not success:

            return {
                "transcript": user_text,
                "response_text": ai_text,
                "audio_file": None,
                "status": "TTS Gagal"
            }

        return {
            "transcript": user_text,
            "response_text": ai_text,
            "audio_file": output_audio,
            "status": "Selesai"
        }

    except Exception as e:

        return {
            "transcript": "",
            "response_text": "",
            "audio_file": None,
            "status": f"Error: {str(e)}"
        }