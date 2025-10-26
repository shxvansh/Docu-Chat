import pdfplumber
import os
import tempfile
from fastapi import HTTPException
from utils.text_utils import clean_text, split_text_into_chunks

def extract_text_from_pdf(file_path: str) -> str:
    """Extract text from PDF file using pdfplumber"""
    try:
        with pdfplumber.open(file_path) as pdf:
            text = ""
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
            return text.strip()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error extracting text from PDF: {str(e)}")

def process_pdf_file(file_content: bytes, filename: str) -> tuple[str, int]:
    """
    Process uploaded PDF file and return document ID and chunk count.
    
    Args:
        file_content: Raw file content
        filename: Original filename
        
    Returns:
        tuple: (document_id, chunk_count)
    """
    # Validate file type
    if not filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    
    # Create temporary file to store uploaded PDF
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_file:
        temp_file.write(file_content)
        temp_file_path = temp_file.name
    
    try:
        # Extract text from PDF
        raw_text = extract_text_from_pdf(temp_file_path)
        
        # Clean the text
        cleaned_text = clean_text(raw_text)
        
        # Validate extracted text
        if not cleaned_text or len(cleaned_text.strip()) < 10:
            raise HTTPException(status_code=400, detail="No readable text found in PDF")
        
        # Split text into chunks
        chunks = split_text_into_chunks(cleaned_text, chunk_size=500, overlap=50)
        
        # TODO: Store chunks for Level 4 (vector embeddings)
        # For now, we'll just return the count
        
        return cleaned_text, len(chunks)
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing PDF: {str(e)}")
    finally:
        # Clean up temporary file
        if os.path.exists(temp_file_path):
            os.unlink(temp_file_path)
