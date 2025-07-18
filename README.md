# EQTRv1

Delmar Horse Management application.

## Development

Build and start services (frontend dependencies are installed during the Docker build so the app runs offline):

```bash
docker-compose -f docker/docker-compose.yml up --build
```

Backend runs at `http://localhost:8000`, frontend at `http://localhost:3000`.
The admin interface is available under `/admin` on the frontend.
Within the admin area you can enable demo data with the **Use demo data**
checkbox. When disabled, the UI will load real data from the API instead.

API calls expect simple role headers:

```
X-Role: admin|owner|viewer
X-Owner-Id: <owner id>  # only for owner role
```
