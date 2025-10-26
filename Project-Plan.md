# Docu-Chat API - RAG Document Q&A System

A FastAPI-based API that allows users to upload documents and ask questions about them using the RAG (Retrieval-Augmented Generation) pattern.

## 🎯 Project Overview

The Docu-Chat API enables users to:
- Upload PDF documents
- Ask questions about the uploaded content
- Get AI-powered answers based on document context

## 🛠 Tech Stack

- **Backend**: FastAPI
- **Document Loading**: pdfplumber
- **Text Splitting**: Custom text splitter
- **Vector Database**: ChromaDB
- **Embedding Model**: Hugging Face Sentence-Transformer (all-MiniLM-L6-v2)
- **LLM**: OpenAI API
- **Data Validation**: Pydantic

## 📋 Project Levels

### ✅ Level 1: Setup & Basic Server (COMPLETED)
- [x] Set up Python virtual environment
- [x] Created `requirements.txt` with all dependencies
- [x] Built basic "Hello World" FastAPI server
- [x] Added comprehensive `.gitignore` file
- [x] Resolved git history issues with large files

**Files Created:**
- `requirements.txt` - Project dependencies
- `main.py` - Basic FastAPI server
- `.gitignore` - Git ignore rules

### 🔄 Level 2: API Endpoints & Models (IN PROGRESS)
- [ ] Create Pydantic models for request/response bodies
- [ ] Add `POST /upload/` endpoint (placeholder)
- [ ] Add `POST /chat/` endpoint (placeholder)
- [ ] Both endpoints return simple JSON success messages

**Planned Models:**
- `UploadResponse` - Response for document upload
- `ChatQuery` - Request body for chat endpoint
- `ChatResponse` - Response for chat endpoint

### ⏳ Level 3: Document Ingestion (Text Processing)
- [ ] Implement PDF file upload handling in `/upload/` endpoint
- [ ] Use `pdfplumber` to extract text from uploaded PDFs
- [ ] Create text splitting logic (500 characters per chunk, 50-character overlap)
- [ ] Process and validate extracted text

### ⏳ Level 4: Embedding & Storage (Vector DB)
- [ ] Initialize sentence-transformers model (`all-MiniLM-L6-v2`)
- [ ] Set up persistent ChromaDB client and create collection
- [ ] Convert text chunks to vector embeddings
- [ ] Store embeddings + metadata in ChromaDB

### ⏳ Level 5: Retrieval Logic
- [ ] Implement question embedding in `/chat/` endpoint
- [ ] Query ChromaDB with question vector
- [ ] Retrieve top 3 most relevant text chunks
- [ ] Return retrieved context

### ⏳ Level 6: Generation Logic (RAG)
- [ ] Construct prompt with retrieved context + user question
- [ ] Integrate OpenAI API call
- [ ] Generate final answer using LLM
- [ ] Return structured response

### ⏳ Level 7: Full Integration & Testing
- [ ] Connect all components from Levels 3-6
- [ ] Replace placeholder logic with full implementation
- [ ] Test end-to-end flow using FastAPI Swagger docs
- [ ] Handle error cases and edge scenarios

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- Git

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Docu-Chat
   ```

2. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the server:
   ```bash
   python main.py
   ```

5. Access the API:
   - API: `http://localhost:8000/`
   - Interactive docs: `http://localhost:8000/docs`
   - Health check: `http://localhost:8000/health`

## 📁 Project Structure

```
Docu-Chat/
├── main.py              # FastAPI application
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore rules
├── README.md           # This file
└── venv/              # Virtual environment (ignored by git)
```

## 🔧 Dependencies

- `fastapi==0.104.1` - Web framework
- `uvicorn[standard]==0.24.0` - ASGI server
- `chromadb==0.4.18` - Vector database
- `openai==1.3.7` - OpenAI API client
- `pdfplumber==0.10.3` - PDF text extraction
- `sentence-transformers==2.2.2` - Embedding models
- `pydantic==2.5.0` - Data validation
- `python-multipart==0.0.6` - File upload support

## 🎯 API Endpoints (Planned)

### POST /upload/
Upload a PDF document for processing.

**Request:**
- `file`: PDF file (multipart/form-data)

**Response:**
```json
{
  "message": "Document uploaded successfully",
  "document_id": "uuid",
  "chunks_created": 42
}
```

### POST /chat/
Ask a question about uploaded documents.

**Request:**
```json
{
  "question": "What is the main topic of the document?",
  "document_id": "uuid"
}
```

**Response:**
```json
{
  "answer": "The main topic is...",
  "sources": ["chunk_1", "chunk_2"],
  "confidence": 0.85
}
```

## 🔍 RAG Architecture

```
PDF Upload → Text Extraction → Text Chunking → Embedding Generation → Vector Storage
                                                                    ↓
User Question → Question Embedding → Vector Search → Context Retrieval → LLM Generation → Answer
```

## 📝 Development Notes

- Virtual environment is properly ignored by git
- Large files (PyTorch models) are excluded from repository
- Clean git history maintained
- Ready for collaborative development

## 🚧 Current Status

**Level 1 Complete** ✅
- Basic FastAPI server running
- Dependencies installed
- Git repository properly configured

**Next Steps:**
- Begin Level 2: Create API endpoints and Pydantic models
- Implement placeholder logic for upload and chat endpoints

---

*Last updated: Level 1 completion*
