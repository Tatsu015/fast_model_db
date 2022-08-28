.PHONY
create_db:
	sqlite3 db/user.db < db/user.sql

.PHONY
dev:
	uvicorn main:app --reload
