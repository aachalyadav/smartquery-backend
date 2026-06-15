# SmartQuery Backend

A modular FastAPI-based backend application designed for prompt processing and AI-powered response generation. This project demonstrates backend API development, request validation, service-layer architecture, and scalable code organization for LLM-powered applications.

## Overview

SmartQuery Backend provides REST API endpoints that accept user prompts, process them through a structured backend pipeline, and return generated responses. The architecture is designed to be clean, modular, and easy to extend with real Large Language Model (LLM) integrations such as OpenAI, Claude, or Ollama.

## Features

* FastAPI-powered REST API
* Modular project architecture
* Request validation using Pydantic
* Service layer for response generation
* Prompt-based response handling
* Easy integration with real AI models

## Project Structure

```bash
smartquery-api/
│
├── app/
│   ├── main.py
│   ├── routes.py
│   ├── models.py
│   └── services.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## API Endpoints

### Home Route

```http
GET /
```

Response:

```json
{
  "message": "Hello! SmartQuery API is running"
}
```

### Ask Route

```http
POST /ask
```

Request Body:

```json
{
  "user_question": "What is AI?"
}
```

Example Response:

```json
{
  "your_question": "What is AI?",
  "answer": "AI stands for Artificial Intelligence. It enables machines to think and learn."
}
```

## Tech Stack

* Python
* FastAPI
* Uvicorn
* Pydantic
* Git & GitHub

## Installation

Clone the repository:

```bash
git clone https://github.com/aachalyadav/smartquery-backend.git
```

Navigate to project directory:

```bash
cd smartquery-backend
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

**Windows**

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run server:

```bash
uvicorn app.main:app --reload
```

## Future Improvements

* Chat history support
* Response analytics
* LLM integration (OpenAI / Claude / Ollama)
* Authentication and database support

## Learning Outcomes

This project strengthened my understanding of:

* Backend architecture
* API development
* Request-response lifecycle
* Code modularization
* Git and GitHub workflow
