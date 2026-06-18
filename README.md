# 🚀 LearnTube AI

### LLM-Powered Retrieval-Augmented Generation (RAG) System for YouTube Courses

LearnTube AI is an end-to-end Retrieval-Augmented Generation (RAG) system that transforms YouTube course content into a searchable knowledge base. The system automatically extracts audio from YouTube playlists, transcribes videos into text, generates vector embeddings, retrieves the most relevant content using semantic search, and produces context-aware answers using a Large Language Model (LLM).

Users can ask questions in natural language and receive concise answers along with the relevant video source and timestamps.

---

## ✨ Features

* 🎥 Extract audio from YouTube playlists using **yt-dlp**
* 🎙️ Convert audio into text using **OpenAI Whisper**
* 📝 Generate structured JSON transcripts with timestamps
* 🧠 Create vector embeddings using **BGE-M3**
* 🔍 Retrieve relevant content using **Cosine Similarity**
* 🤖 Generate answers using **Llama 3.2 via Ollama**
* ⏱️ Return video names and timestamps for retrieved content
* 💻 Fully local AI pipeline

---

## 🏗️ System Architecture

```text
YouTube Playlist
        ↓
Audio Extraction (yt-dlp)
        ↓
Speech-to-Text (Whisper)
        ↓
JSON Transcript Generation
        ↓
Embedding Generation (BGE-M3)
        ↓
Semantic Retrieval (Cosine Similarity)
        ↓
Top Relevant Chunks
        ↓
Llama 3.2 (Ollama)
        ↓
Answer + Video Reference + Timestamp
```

---

## 🛠️ Tech Stack

| Technology   | Purpose                  |
| ------------ | ------------------------ |
| Python       | Core Development         |
| Whisper      | Speech-to-Text           |
| Ollama       | Local LLM Inference      |
| BGE-M3       | Embeddings               |
| Llama 3.2    | Answer Generation        |
| Pandas       | Data Processing          |
| NumPy        | Numerical Computation    |
| Scikit-Learn | Cosine Similarity        |
| yt-dlp       | YouTube Audio Extraction |
| FFmpeg       | Audio Conversion         |

---

## 📂 Project Structure

```text
LearnTube-AI/
│
├── 01_load_webm_from_youtube.py
├── 02_webm_to_mp3.py
├── 03_mp3_to_jsons.py
├── 04_chunking.py
├── 05_process_query.py
├── 06_llm_response.py
│
├── videos_webm/
├── audios_mp3/
├── jsons/
│
├── chunks.pkl
├── prompt.txt
├── response.txt
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 💡 Example Query

### User Question

```text
Where is Next.js Authentication explained?
```

### Example Output

```text
Authentication is explained in the video:

Video:
Complete Next.js Fullstack Authentication Course

Timestamp:
12:45 - 15:32

Summary:
Authentication is implemented using ...
```

---

## 📋 Prerequisites

- Python 3.13+
- FFmpeg installed and available in PATH
- Ollama installed

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/LearnTube-AI.git
cd LearnTube-AI
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Install Ollama

Download and install Ollama from:

https://ollama.com

Pull required models:

```bash
ollama pull bge-m3
ollama pull llama3.2:3b
```

---

## 🚀 Usage

### Step 1: Download Audio from YouTube Playlist

```bash
python 01_load_webm_from_youtube.py
```

### Step 2: Convert Audio Files

```bash
python 02_webm_to_mp3.py
```

### Step 3: Generate Transcripts

```bash
python 03_mp3_to_jsons.py
```

### Step 4: Generate Embeddings

```bash
python 04_chunking.py
```

### Step 5: Process User Query

```bash
python 05_process_query.py
```

### Step 6: Generate Final Answer

```bash
python 06_llm_response.py
```

---

## 🚧 Future Improvements

### 🎙️ Better Speech Recognition

Current implementation uses the Whisper Base model.

Possible upgrades:

* Whisper Large-v2
* Whisper Large-v3

for higher transcription accuracy.

---

### 🧩 Improved Chunking Strategy

Retrieval quality can be improved by:

* Merging multiple transcript segments
* Creating larger semantic chunks
* Introducing chunk overlap
* Applying advanced text-splitting techniques

---

### 🧠 Better Embedding Models

Potential upgrades:

* OpenAI Embeddings
* Voyage AI Embeddings
* Nomic Embed
* Other state-of-the-art embedding models

---

### ⚡ Advanced Vector Search

Current implementation uses Cosine Similarity.

Future versions may integrate:

* FAISS
* ChromaDB
* Qdrant
* Pinecone

for faster and more scalable retrieval.

---

### 🤖 More Powerful Language Models

Current implementation uses Llama 3.2 through Ollama.

Future versions may support:

* GPT-5
* Claude
* Gemini
* DeepSeek
* Qwen
* Larger Llama Models

through API-based or self-hosted deployments.

---

## 🙏 Acknowledgements

This project uses educational content from **Hitesh Choudhary's Next.js Full Stack Course** on YouTube for learning, experimentation, and research purposes.

Special thanks to **Hitesh Choudhary** for creating high-quality educational content that made this project possible.

This repository does not redistribute any original course content and is intended solely for educational and research purposes.

---

## 🎯 Motivation

The goal of this project is to explore modern AI application development by combining speech recognition, embeddings, retrieval systems, and large language models into a practical educational tool.

LearnTube AI demonstrates how long-form educational video content can be transformed into an interactive knowledge base capable of answering questions with source attribution and timestamps.

---

## 📜 License

This project is intended for educational and research purposes.
