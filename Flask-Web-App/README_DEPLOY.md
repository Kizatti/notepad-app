Deploying this Flask notes app (Vercel using Docker)
===============================================

This project can be deployed to Vercel using the included Dockerfile and `vercel.json` which tell Vercel to build the container.

Quick steps (Vercel)
1. Push your repository to GitHub.
2. In Vercel, create a new project and import the GitHub repo.
3. Vercel should detect the `vercel.json` and build the Docker image using the `Dockerfile`.
4. Set environment variables in the Vercel dashboard for your project:
   - `SECRET_KEY` — a secure random string
   - `DATABASE_URL` — (optional) a Postgres connection string if you add a managed database; otherwise app will use SQLite in the container (not recommended for multi-instance deployments).
5. Deploy and open the assigned URL. Monitor logs from the Vercel dashboard.

Notes and recommendations
- For production use a managed Postgres instance (set `DATABASE_URL`) instead of the default SQLite file.
- Use a secure `SECRET_KEY` stored in Vercel environment variables.
- Consider adding migrations (Flask-Migrate) if you evolve the database schema.
- For local testing with Docker:
  - docker build -t notes-app .
  - docker run -e SECRET_KEY="your-secret" -e PORT=8080 -p 8080:8080 notes-app

If you'd like, I can add a `Procfile`, `runtime.txt` (Python version), or a small `docker-compose.yml` for local multi-service testing (Postgres + app).
