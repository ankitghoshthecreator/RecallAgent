LangChain
   ↓
RAG components / document processing / integrations

LangGraph
   ↓
Agent workflow / state machine

ChromaDB
   ↓
Vector similarity search

Sentence Transformers
   ↓
Embedding generation

Neo4j
   ↓
Knowledge graph

PyPDF
   ↓
Read PDF documents

python-dotenv
   ↓
API keys / configuration

FastAPI
   ↓
Backend API



## Step 2 — Build the simplest RAG

Once ingestion works, implement:

Query
 ↓
Embedding
 ↓
Vector search
 ↓
Top-k chunks
 ↓
LLM
 ↓
Answer

![img.png](img.png)

## Step 2 — Embeddings

The goal is to turn every chunk into a numerical vector:

![img_1.png](img_1.png)

Our pipeline becomes
                    Documents
                        ↓
                     Chunking
                        ↓
              ┌─────────┴─────────┐
              ↓                   ↓
           Chunks             Query
              ↓                   ↓
          Embedding           Embedding
              ↓                   ↓
              └─────────┬─────────┘
                        ↓
                 Similarity Search
                        ↓
                     Top-k
                        ↓
                  Relevant chunks

## Step 3 — Vector Search

Our goal is:

User Query
    ↓
Query embedding
    ↓
Compare against all chunk embeddings
    ↓
Calculate similarity
    ↓
Sort by similarity
    ↓
Return Top-K chunks