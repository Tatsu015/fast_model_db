setup:
	python3 -m venv . && \
	source bin/activate && \
	pip install -r requirements.txt && \
	sqlite3 db/users.db < db/users.sql

dev:
	uvicorn main:app --reload

db_clean:
	git clean -fdx db

db_create:
	sqlite3 db/users.db < db/users.sql

full_clean:
	git clean -fdx
