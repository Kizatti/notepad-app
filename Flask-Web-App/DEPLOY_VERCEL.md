# Deploying to Vercel

This guide explains how to deploy your Flask Notes app to Vercel using serverless Python functions.

## Pre-deployment Setup

1. Requirements are already in `requirements.txt`
2. Vercel configuration is in `vercel.json`
3. Serverless functions are in the `api/` directory

## Deploy to Vercel

1. Push your code to GitHub if you haven't already.

2. Go to [Vercel](https://vercel.com) and:
   - Create an account or log in
   - Click "New Project"
   - Import your GitHub repository
   - Select "Python" as the framework

3. Configure Environment Variables:
   - Click "Environment Variables"
   - Add the following:
     ```
     SECRET_KEY=<your-secure-random-string>
     DATABASE_URL=<your-postgres-connection-string>
     ```
   Note: For PostgreSQL, you can use:
   - Vercel Postgres
   - Railway.app
   - Supabase
   - Any PostgreSQL provider

4. Click "Deploy"

## Important Notes

1. Database:
   - SQLite cannot be used (Vercel has no persistent filesystem)
   - Use PostgreSQL (recommended) via DATABASE_URL
   - Your database must be accessible from Vercel's servers

2. Sessions/Login:
   - Uses Flask-Login with cookie-based sessions
   - No filesystem session storage (serverless environment)

3. Static Files:
   - Served through the `/static` route configuration
   - Vercel handles caching automatically

## Local Development

1. Set environment variables:
   ```bash
   $env:SECRET_KEY="your-dev-key"
   $env:DATABASE_URL="postgresql://user:pass@localhost:5432/dbname"
   ```

2. Run the development server:
   ```bash
   python main.py
   ```

## Troubleshooting

1. If deployment fails:
   - Check Vercel build logs
   - Verify environment variables are set
   - Ensure DATABASE_URL is accessible from Vercel

2. If app crashes:
   - Check Vercel logs in dashboard
   - Verify database connection
   - Check for environment variable issues

3. If static files 404:
   - Verify paths in templates use url_for()
   - Check vercel.json routes configuration

Need help? See [Vercel Python docs](https://vercel.com/docs/serverless-functions/supported-languages#python)