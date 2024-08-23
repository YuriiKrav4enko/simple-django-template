DB_DC_FILE = docker_compose/database.yaml
BACKEND_DC_FILE = docker_compose/backend.yaml
DB_CONTAINER = "project-db"
BACKEND_CONTAINER = "backend-app"

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

.PHONY: backend-image
backend-image:
	docker build -t backend_app .

.PHONY: backend
backend:
	docker compose -f ${BACKEND_DC_FILE} -f ${DB_DC_FILE} up -d

.PHONY: backend-logs
backend-logs:
	docker logs ${BACKEND_CONTAINER} -f

.PHONY: backend-stop
backend-stop:
	docker compose -f ${BACKEND_DC_FILE} -f ${DB_DC_FILE} down

.PHONY: migrate
migrate:
	docker exec -it ${BACKEND_CONTAINER} ./manage.py migrate

.PHONY: superuser
superuser:
	docker exec -it ${BACKEND_CONTAINER} ./manage.py createsuperuser
