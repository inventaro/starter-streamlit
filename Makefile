.PHONY: up down logs login upin

upin: up login

up:
	@echo "Starting server..."
	docker compose -f docker-compose_dev.yml up -d --build

login:
	@echo "Logging in to container..."
	docker compose -f docker-compose_dev.yml exec streamlit bash

down:
	@echo "Stopping server..."
	docker compose -f docker-compose_dev.yml down

logs:
	@echo "Logs..."
	docker compose -f docker-compose_dev.yml logs -f streamlit

