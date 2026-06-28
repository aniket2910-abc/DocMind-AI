# 📄 DocMind-AI

link for the main website- https://melodious-gumdrop-ff9161.netlify.app

An AI-powered PDF Question Answering application that allows users to upload PDF documents, ask questions, and receive intelligent answers generated using a Retrieval-Augmented Generation (RAG) pipeline.

---

## 🚀 Features

- 📄 Upload PDF documents
- 🤖 AI-powered question answering
- 🧠 Retrieval-Augmented Generation (RAG)
- 🔍 Semantic document search using embeddings
- 💬 Interactive chat interface
- ⚡ Fast and responsive React + Vite frontend
- 🐍 Python backend with REST API
- 📑 Markdown formatted AI responses

---

## 🛠 Tech Stack

### Frontend
- React.js
- Vite
- Axios
- React Markdown
- CSS

### Backend
- Python
- FastAPI
- LangChain
- Sentence Transformers
- FAISS Vector Store
- PyPDF
- Uvicorn

---

## 📂 Project Structure

```
DocMind-AI/
│
├── backend/
│   ├── main.py
│   ├── rag.py
│   ├── pdf_loader.py
│   ├── embeddings.py
│   ├── vector_store.py
│   └── llm.py
│
├── public/
│
├── src/
│   ├── components/
│   ├── pages/
│   ├── api.js
│   ├── App.jsx
│   └── main.jsx
│
├── package.json
├── vite.config.js
└── README.md
```

---

## ⚙ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/DocMind-AI.git
cd DocMind-AI
```

---

## Install Frontend

```bash
npm install
```

Run Frontend

```bash
npm run dev
```

---

## Install Backend

```bash
cd backend

pip install -r requirements.txt
```

Run Backend

```bash
uvicorn main:app --reload
```

---

## 🌐 API Endpoint

```
POST /upload
```

Upload PDF documents.

```
POST /chat
```

Ask questions related to the uploaded document.

---

## 💡 How It Works

1. Upload a PDF.
2. PDF text is extracted.
3. Text is converted into vector embeddings.
4. Embeddings are stored in a FAISS vector database.
5. User asks a question.
6. Relevant document chunks are retrieved.
7. LLM generates a contextual answer.
8. Response is displayed in the chat interface.

---

## 📸 Screenshots

<img width="1896" height="893" alt="image" src="https://github.com/user-attachments/assets/b94d1ac7-ae17-42f1-b0f2-e505953d7893" />
<img width="1898" height="882" alt="image" src="https://github.com/user-attachments/assets/b5745dce-514a-4351-a852-ba5f3c9a0c8c" />
<img width="1892" height="781" alt="image" src="https://github.com/user-attachments/assets/d98f753d-b601-4a60-931b-353020607158" />


---

## 🔮 Future Improvements

- Multiple PDF support
- User Authentication
- Chat History
- Cloud Storage
- Citation & Source Highlighting
- Dark Mode
- Streaming AI Responses
- Multi-language Support

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Developer

**Aniket Kumar Singh**

- AI & ML Student
- Python Developer
- Full Stack AI Enthusiast

GitHub: https://github.com/aniket2910-abc

---

⭐ If you like this project, don't forget to give it a Star!
