setup:
	python3 -m venv . && \
	source bin/activate && \
	pip install -r requirements.txt && \
	sqlite3 db/user.db < db/user.sql
dev:
	uvicorn main:app --reload
clean:
	git clean -fdx db
full_clean:
	git clean -fdx
