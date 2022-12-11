.PHONY:docker_build
docker_build:
	docker build -t fmd/latest .

.PHONY:up
up:
	docker compose --env-file .devcontainer/.env up

.PHONY:migrate
migrate:
	docker exec fast_model_db-app-1 alembic upgrade head


# setup:
# 	python3 -m venv . && \
# 	source bin/activate && \
# 	pip install -r requirements.txt && \
# 	sqlite3 db/users.db < db/users.sql

# dev:
# 	uvicorn fast_model_db.main:app --reload

# db_clean:
# 	git clean -fdx db

# db_create:
# 	sqlite3 db/users.db < db/users.sql

# full_clean:
# 	git clean -fdx
