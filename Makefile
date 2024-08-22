DB_DC_FILE = docker_compose/database.yaml
DB_CONTAINER = "project-db"

.PHONY: db
db:
	docker compose -f ${DB_DC_FILE} up -d

.PHONY: db-stop
db-stop:
	docker compose -f ${DB_DC_FILE} down

.PHONY: db-logs
db-logs:
	docker logs ${DB_CONTAINER} -f

.PHONY: db-conn
db-conn:
	docker exec -it ${DB_CONTAINER} psql -U myuser