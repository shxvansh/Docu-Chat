from pydantic import BaseModel
from typing import List

class ChatQuery(BaseModel):
    """Request model for chat endpoint"""
    question: str
    document_id: str

class UploadResponse(BaseModel):
    """Response model for upload endpoint"""
    message: str
    document_id: str
    chunks_created: int

class ChatResponse(BaseModel):
    """Response model for chat endpoint"""
    answer: str
    sources: List[str]
    confidence: float
