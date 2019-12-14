init:
	pip install -r requirements.txt

db:
	@echo shutting down docker with database if exists
	docker-compose down
	sleep 3
	@echo raising up docker with database
	docker-compose up -d
	sleep 5
	@echo adding procedures
	psql -h localhost -d db -U jordan -q < resources/also.sql
	@echo applying data from dump
	psql -h localhost -d db -U jordan -q < resources/dump.sql

start:
	make init
	make db
	@echo starting service...
	python3 main.py

restart:
	python3 main.py

help:
	@echo "Available targets:"
	@echo "- init       Install all required for project libraries"
	@echo "- db         Init database with data from dump"
	@echo "- start      Start service"
	@echo "- restart    Restart service"
