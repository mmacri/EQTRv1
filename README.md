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

## Database and migrations

Alembic manages database migrations. Run the migrations inside the backend
service with:

```bash
docker-compose -f docker/docker-compose.yml run --rm backend alembic upgrade head
```

The SQLite database file lives at `backend/db/data.db` (inside the container it
resides in `/app/db/data.db`).

## Admin UI and demo data

The admin data grid is served at `http://localhost:3000/grid`. You can populate
the app with sample content by toggling "Demo data" in the UI before
initialization.
