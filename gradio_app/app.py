import gradio as gr
import requests

API_URL = "http://127.0.0.1:8000/voice-chat"


def process_audio(audio_path):

    if audio_path is None:

        return (
            "",
            "",
            None,
            "Tidak ada audio yang diberikan"
        )

    try:

        with open(audio_path, "rb") as f:

            files = {
                "audio": f
            }

            response = requests.post(
                API_URL,
                files=files,
                timeout=300
            )

        data = response.json()

        transcript = data.get(
            "transcript",
            ""
        )

        response_text = data.get(
            "response_text",
            ""
        )

        audio_file = data.get(
            "audio_file",
            None
        )

        status = data.get(
            "status",
            "Selesai"
        )

        return (
            transcript,
            response_text,
            audio_file,
            status
        )

    except Exception as e:

        return (
            "",
            "",
            None,
            f"Error: {str(e)}"
        )


with gr.Blocks(
    title="Multilingual Speech-to-Speech System"
) as demo:

    gr.Markdown(
        """
        # 🎙️ Multilingual Speech-to-Speech System
        
        Whisper → Gemini → Coqui TTS
        
        Bahasa Indonesia • English • العربية
        """
    )

    audio_input = gr.Audio(
        sources=["microphone"],
        type="filepath",
        label="🎤 Input Audio"
    )

    submit_btn = gr.Button(
        "🚀 Process"
    )

    transcript_output = gr.Textbox(
        label="📝 Transcript (STT)",
        lines=4
    )

    response_output = gr.Textbox(
        label="🤖 Response (LLM)",
        lines=6
    )

    audio_output = gr.Audio(
        label="🔊 Response Audio"
    )

    status_output = gr.Textbox(
        label="📊 Status"
    )

    submit_btn.click(
        fn=process_audio,
        inputs=audio_input,
        outputs=[
            transcript_output,
            response_output,
            audio_output,
            status_output
        ]
    )

if __name__ == "__main__":

    demo.launch(
        server_name="127.0.0.1",
        server_port=7860,
        share=False
    )