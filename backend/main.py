from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
import traceback

from pydantic import BaseModel
from pypdf import PdfReader

from pdf_loader import load_pdf
from embeddings import get_embeddings
from vector_store import create_vector_store
from rag import get_prompt, format_docs
from llm import ask_gemini

app = FastAPI(
    title="Enterprise Knowledge Assistant",
    version="1.0.0"
)

# =========================
# CORS
# =========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://melodious-gumdrop-ff9161.netlify.app",

    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

vector_db = None
embeddings = get_embeddings()


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "Enterprise Knowledge Assistant API is Running 🚀"
    }


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    global vector_db

    try:

        file_path = os.path.join(
            UPLOAD_FOLDER,
            file.filename
        )

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        print("✅ PDF Saved:", file_path)

        # Total Pages
        reader = PdfReader(file_path)
        total_pages = len(reader.pages)

        # Split PDF
        chunks = load_pdf(file_path)

        print("✅ Total Pages:", total_pages)
        print("✅ Total Chunks:", len(chunks))

        vector_db = create_vector_store(
            chunks,
            embeddings
        )

        print("✅ Vector Store Created")

        return {
            "message": "PDF Uploaded Successfully",
            "filename": file.filename,
            "pages": total_pages,
            "chunks": len(chunks)
        }

    except Exception as e:
        traceback.print_exc()

        return {
            "error": str(e)
        }


@app.post("/ask")
async def ask_question(request: QuestionRequest):

    global vector_db

    try:

        if vector_db is None:
            return {
                "error": "Please upload a PDF first."
            }

        print("================================")
        print("Question:", request.question)

        docs = vector_db.similarity_search(
            request.question,
            k=4
        )

        print("Retrieved Docs:", len(docs))

        context = format_docs(docs)

        prompt = get_prompt().format(
            context=context,
            question=request.question
        )

        print("Prompt Created Successfully")

        answer = ask_gemini(prompt)

        print("Gemini Response Received")

        return {
            "question": request.question,
            "answer": answer
        }

    except Exception as e:

        print("\n❌ ERROR INSIDE /ask\n")

        traceback.print_exc()

        return {
            "error": str(e)
        }