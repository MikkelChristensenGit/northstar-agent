.PHONY: pipelines qdrant-up qdrant-down

setup:
	uv sync

data_pipeline:
	uv run python -m src.data_processing.pipeline

ingest_pipeline:
	uv run python -m src.ingest.pipeline

app:
	uv run uvicorn src.router.response:app --reload

FAST_API_URL ?= http://127.0.0.1:8000
chatq:
	@read -r -p "Question: " q; \
	payload=$$(python -c 'import json,sys; print(json.dumps({"question": sys.argv[1]}))' "$$q"); \
	curl -s -X POST "$(FAST_API_URL)/chat" \
		-H 'Content-Type: application/json' \
		-d "$$payload"; \
	echo

qdrant-up:
	@docker start northstar-qdrant 2>/dev/null || \
	docker run -d --name northstar-qdrant \
		-p 6333:6333 -p 6334:6334 \
		-v northstar_qdrant_storage:/qdrant/storage \
		qdrant/qdrant:latest

qdrant-down:
	docker stop northstar-qdrant
