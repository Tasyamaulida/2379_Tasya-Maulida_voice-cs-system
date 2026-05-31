import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

API_KEYS = []

for i in range(1, 51):

    key = os.getenv(f"GEMINI_API_KEY_{i}")

    if key:
        API_KEYS.append(key)
        
API_KEYS = [k for k in API_KEYS if k]

if not API_KEYS:
    raise ValueError("Tidak ada API KEY ditemukan")

current_key = 0


def get_client():
    return genai.Client(
        api_key=API_KEYS[current_key]
    )


def rotate_key():

    global current_key

    current_key += 1

    if current_key >= len(API_KEYS):

        print("\nSEMUA API KEY SUDAH HABIS")

        return False

    print(
        f"\nPINDAH KE API KEY #{current_key + 1}"
    )

    return True


def get_chatbot_response(user_text):

    global current_key

    if not user_text:
        return "Ahlan! Ada yang bisa saya bantu?"

    prompt = f"""
Kamu adalah asisten multilingual Indonesia-English-Arabic.

Aturan:
- Jawab singkat dan jelas.
- Pertahankan code-switching jika ada.
- Jika ada kata Arab, jangan diterjemahkan.
- Fokus menjawab pertanyaan pengguna.

User:
{user_text}
"""

    while True:

        try:

            client = get_client()

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            return response.text

        except Exception as e:

            print(f"DEBUG Error Gemini: {e}")

            error_text = str(e)

            if (
                "429" in error_text
                or "403" in error_text
                or "RESOURCE_EXHAUSTED" in error_text
                or "PERMISSION_DENIED" in error_text
            ):

                if rotate_key():
                    continue

                return "ERROR_QUOTA"

            return "ERROR_GEMINI"


if __name__ == "__main__":

    test_text = "Aku mau booking flight ke Jeddah minggu depan"

    result = get_chatbot_response(
        test_text
    )

    print(result)