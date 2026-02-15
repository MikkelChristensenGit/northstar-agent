# Northstar RAG API (POC)

This repository is a poc for a QnA AI agent on the Northstar material and exposes the agent through a FastAPI endpoint.

## Run locally


Before starting the API, install dependencies with `make setup`, create the data with `data_pipeline start`, start Qdrant with `make qdrant-up`, and run `make ingest_pipeline` to populate the vector store.

Start the API:

```
make app
```

Test the chat endpoint:

```
make chatq
```
and type a question.

A brief Swagger documentation can be found on http://127.0.0.1:8000/docs providing an example and defined schemas.
