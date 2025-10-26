from fastapi import FastAPI
import uvicorn

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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
