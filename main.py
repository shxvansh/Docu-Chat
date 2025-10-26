from fastapi import FastAPI, UploadFile, File
import uvicorn
import uuid
from models import ChatQuery, UploadResponse, ChatResponse
from services.pdf_service import process_pdf_file

# Create FastAPI instance
app = FastAPI(
    title="Docu-Chat API",
    description="A RAG-based API for document Q&A",
    version="1.0.0"
)

@app.get("/")
async def root():
    """Root endpoint - Hello World"""
    return {"message": "Hello World! Docu-Chat API is running!"}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "message": "API is running successfully"}

@app.post("/upload/", response_model=UploadResponse)
async def upload_document(file: UploadFile = File(...)):
    """
    Upload a PDF document for processing.
    
    Level 3 implementation: Extract text from PDF and split into chunks.
    """
    # Generate document ID
    document_id = str(uuid.uuid4())
    
    # Read uploaded file content
    content = await file.read()
    
    # Process PDF file
    _, chunks_created = process_pdf_file(content, file.filename)
    
    return UploadResponse(
        message="Document uploaded and processed successfully",
        document_id=document_id,
        chunks_created=chunks_created
    )

@app.post("/chat/", response_model=ChatResponse)
async def chat_with_document(query: ChatQuery):
    """
    Ask a question about uploaded documents.
    
    This is a placeholder endpoint that will be implemented in Levels 5-6.
    For now, it returns a mock answer with placeholder data.
    """
    # Placeholder response - actual RAG implementation will be in Levels 5-6
    return ChatResponse(
        answer=f"This is a placeholder response for the question: '{query.question}'. The actual RAG implementation will be added in Level 6.",
        sources=["chunk_1", "chunk_2"],  # Mock sources
        confidence=0.85  # Mock confidence score
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
