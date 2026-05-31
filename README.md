# 2379_Tasya-Maulida_voice-cs-system
Multilingual Speech-to-Speech System using Whisper, Gemini API, and Coqui TTS for Indonesian-English-Arabic Code-Switching Conversations.

# 🎙️ Multilingual Speech-to-Speech System

## 📌 Deskripsi Project

Multilingual Speech-to-Speech System merupakan sistem percakapan berbasis suara yang mampu menerima masukan berupa audio, melakukan transkripsi suara menjadi teks, menghasilkan respons menggunakan Large Language Model (LLM), dan mengubah respons tersebut kembali menjadi suara.

Sistem mendukung percakapan multilingual yang melibatkan Bahasa Indonesia, Bahasa Inggris, dan Bahasa Arab serta mampu menangani fenomena code-switching dalam percakapan sehari-hari.

Project ini dikembangkan sebagai tugas UAS Praktikum Natural Language Processing (NLP) Tahun Akademik 2025/2026.

---

## 🚀 Fitur Utama

- Speech-to-Text menggunakan OpenAI Whisper
- Large Language Model menggunakan Gemini API
- Text-to-Speech menggunakan Coqui TTS
- Mendukung Bahasa Indonesia, Inggris, dan Arab
- Mendukung percakapan Code-Switching
- Antarmuka pengguna menggunakan Gradio
- Backend menggunakan FastAPI
- Batch processing untuk eksperimen dataset
- Output audio dalam format WAV

---

## 🏗️ Arsitektur Sistem

```text
Input Audio
      │
      ▼
Speech-to-Text (Whisper)
      │
      ▼
Text Processing
      │
      ▼
Large Language Model (Gemini)
      │
      ▼
Text-to-Speech (Coqui TTS)
      │
      ▼
Output Audio
```

---

## 📂 Struktur Project

```text
Voice-CS-System/
│
├── app/
│   ├── main.py
│   ├── stt.py
│   ├── llm.py
│   ├── tts.py
│   ├── utils.py
│   │
│   └── coqui_tts/
│       ├── checkpoint_1260000-inference.pth
│       ├── config.json
│       └── speakers.pth
│
├── gradio_app/
│   └── app.py
│
├── data/
│   ├── audio/
│   ├── audio_ai/
│   └── transcripts/
│
├── generate_llm_response.py
├── generate_tts_audio.py
├── analysis_pipeline.py
├── results_sst.csv
├── results_llm.csv
├── requirements.txt
└── README.md
```

---

## ⚙️ Teknologi yang Digunakan

- Python 3.11
- OpenAI Whisper
- Google Gemini API
- Coqui TTS
- FastAPI
- Gradio
- Pandas
- PyTorch

---

## 📥 Instalasi

### Clone Repository

```bash
git clone https://github.com/Tasyamaulida/2379_Tasya-Maulida_voice-cs-system.git
cd 2379_Tasya-Maulida_voice-cs-system
```

### Membuat Virtual Environment

```bash
python -m venv env
```

### Aktivasi Environment

Windows:

```bash
env\Scripts\activate
```

Linux/Mac:

```bash
source env/bin/activate
```

### Install Dependency

```bash
pip install -r requirements.txt
```

---

## 🔑 Konfigurasi API

Buat file `.env`

```env
GEMINI_API_KEY_1=YOUR_API_KEY
GEMINI_API_KEY_2=YOUR_API_KEY
GEMINI_API_KEY_3=YOUR_API_KEY
```

Sistem mendukung rotasi API Key secara otomatis apabila kuota salah satu API telah habis.

---

## ▶️ Menjalankan Backend

```bash
uvicorn app.main:app --reload
```

Backend berjalan pada:

```text
http://127.0.0.1:8000
```

---

## ▶️ Menjalankan Gradio Interface

Buka terminal baru:

```bash
python gradio_app/app.py
```

Aplikasi dapat diakses melalui:

```text
http://127.0.0.1:7860
```

---

## 🧪 Hasil Eksperimen

Dataset yang digunakan terdiri dari:

- 571 data audio multilingual
- Bahasa Indonesia
- Bahasa Inggris
- Bahasa Arab
- Percakapan Code-Switching

Hasil eksperimen:

| Komponen | Hasil |
|-----------|---------|
| Speech-to-Text | Berhasil |
| Gemini Response | Berhasil |
| Text-to-Speech | Berhasil |
| Batch Audio Generation | Berhasil |
| Integrasi Pipeline | Berhasil |
| Gradio Interface | Berhasil |

Sebanyak 571 audio berhasil ditranskripsi, 441 respons berhasil dihasilkan oleh Gemini API, dan 441 file audio berhasil dibuat menggunakan Coqui TTS.

---

## 📸 Contoh Pengujian

Pengujian dilakukan menggunakan antarmuka Gradio.

Pipeline yang berhasil dijalankan:

```text
Audio Input
      ↓
Whisper STT
      ↓
Gemini API
      ↓
Coqui TTS
      ↓
Audio Response
```

Sistem berhasil menghasilkan transkripsi, respons chatbot, dan keluaran suara secara end-to-end.

---

## 👩‍💻 Pengembang

**Tasya Maulida**  
NPM: 2308107010079

Praktikum Natural Language Processing (NLP)  
Jurusan Informatika  
Universitas Syiah Kuala

---

## 📄 Lisensi

Project ini dikembangkan untuk keperluan akademik pada mata kuliah Praktikum Natural Language Processing.
