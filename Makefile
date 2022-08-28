.PHONY
create_db:
	sqlite3 db/user.db < db/user.sql
