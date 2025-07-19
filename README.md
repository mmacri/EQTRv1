# EQTRv1

Delmar Horse Management application.

## Development

### Build and start services

```bash
docker-compose -f docker/docker-compose.yml up --build
```

The backend stores its SQLite database in `backend/db`. This directory is created automatically when the containers start. Backend runs at `http://localhost:8000` and the frontend at `http://localhost:3000`. The frontend container runs an entrypoint script that installs dependencies if `node_modules` is missing before starting Vite.

### Database and migrations

Alembic manages database migrations. Apply them with:

```bash
docker-compose -f docker/docker-compose.yml run --rm backend alembic upgrade head
```

The SQLite database file lives at `backend/db/data.db` (inside the container it resides in `/app/db/data.db`).

### Admin UI and demo data

The admin data grid is served at `http://localhost:3000/grid`. You can populate the app with sample content by toggling "Demo data" in the UI before initialization.

### Running tests

Unit tests live under `backend/app/tests`. Install backend dependencies and run
pytest with `PYTHONPATH` pointing at the `backend` directory so the `app`
package resolves correctly:

```bash
pip install -r backend/requirements.txt
PYTHONPATH=backend pytest
```
