# Doxly

Multitenant group chat with AI document analysis.

Users create workspaces, invite members, chat in channels, upload documents, and query them via `@ai` — the backend retrieves relevant chunks using hybrid search and generates a response through an LLM.

> **Live demo:** _coming soon_



---

## Features

- JWT authentication with registration and login
- Multitenant workspaces with role-based access control (owner / admin / member)
- WebSocket group chat with first-message token auth pattern
- Document upload with background processing pipeline (parse → chunk → embed → store)
- `@ai` mentions trigger hybrid RAG search + LLM response inline in chat
- Permission enforcement via callable FastAPI `Depends` — no decorators, no middleware

---

## Tech Stack

| Layer | Tools |
|---|---|
| API | FastAPI, Pydantic v2 |
| Database | PostgreSQL, SQLAlchemy (async) |
| Vector search | pgvector |
| Embeddings | sentence-transformers (all-MiniLM-L6-v2) |
| LLM | OpenRouter (OpenAI-compatible) |
| Real-time | WebSockets |

---

## Architecture

Route → Service → Repository pattern across independent apps: `auth`, `workspaces`, `chat`, `rag`, `core`.

**RBAC** is implemented as a callable `Permission` class injected via `Depends`. Each route declares required role; the dependency resolves workspace membership and compares roles without touching business logic.

**WebSocket auth** uses a first-message pattern: the client sends a JSON token as the first message after connecting. The connection is rejected if the token is missing or invalid — no HTTP upgrade headers required.

**Hybrid search** is implemented from scratch without libraries. BM25 (TF-IDF with length normalization) and cosine similarity via pgvector run independently. Results are combined as a weighted score fusion: `final_score = cosine_score * 0.6 + bm25_score * 0.4`. Chunks are ranked by final score and top-k are passed to the LLM as context.

**Document pipeline** runs in FastAPI `BackgroundTasks`: upload → text extraction → character-based chunking with overlap → sentence-transformers embedding → pgvector insert.

---

## Project Structure

```
backend/
├── main.py
├── config.py
└── src/
    ├── core/          # DB session, base repository, shared exceptions
    ├── auth/          # JWT, registration use case
    ├── workspaces/    # Workspace and membership management
    ├── chat/          # WebSocket handler, message persistence
    └── rag/           # Chunking, hybrid search, LLM service
```

---

## Running Locally

### Prerequisites

- Docker and Docker Compose
- OpenRouter API key

### Setup

1. Clone the repository

```bash
git clone https://github.com/CodeIsArtNowadays/Doxly.git
cd Doxly
```

2. Create `.env` file in `backend/`

```env
DB_HOST=db
DB_PORT=5432
POSTGRES_DB=doxly
POSTGRES_USER=postgres
POSTGRES_PASSWORD=yourpassword
JWT_SECRET_KEY=your-secret-key
AI_KEY=your-openrouter-key
```

3. Start with Docker Compose

```bash
docker-compose up --build
```

API available at `http://localhost:8000`  
Swagger docs at `http://localhost:8000/docs`

---

## API Overview

| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth/register` | Register new user |
| POST | `/auth/login` | Get JWT token |
| POST | `/workspaces` | Create workspace |
| POST | `/workspaces/{id}/members` | Invite member (owner only) |
| GET | `/workspaces/{id}/channels` | List channels |
| WS | `/chat/{channel_id}` | Connect to channel chat |
| POST | `/workspaces/{id}/documents` | Upload document |
