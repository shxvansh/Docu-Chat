# Docu-Chat API

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

## 📋 Project Plan

For detailed project levels, development roadmap, and technical specifications, see [Project-Plan.md](./Project-Plan.md).

## 🚀 Quick Start

1. Install dependencies: `pip install -r requirements.txt`
2. Run the server: `python main.py`
3. Access the API documentation at `/docs` endpoint