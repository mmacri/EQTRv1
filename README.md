# EQTRv1

Delmar Horse Management application.

## Development

Build and start services:

```bash
docker-compose -f docker/docker-compose.yml up --build
```

The backend stores its SQLite database in `backend/db`. The Dockerfile and
startup routines will create this folder automatically if it does not exist.

Backend runs at `http://localhost:8000`, frontend at `http://localhost:3000`.
