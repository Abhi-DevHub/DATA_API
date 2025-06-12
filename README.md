## Docker

- `docker build -t analytics-api -f Dockerfile.web .`
- `docker run analytics-api `

becomes

- `docker compose up --watch`
- `docker compose down` or `docker compose down -v` (to remove volumes)
- `docker compose run app /bin/bash` or `docker compose run app python` 