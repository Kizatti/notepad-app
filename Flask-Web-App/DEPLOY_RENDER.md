# Deploying to Render.com

This guide walks you through deploying your Flask Notes app to Render.com using your existing Dockerfile.

## Quick Deploy Steps

1. Push your code to GitHub (if you haven't already)

2. Sign up for Render
   - Go to [render.com](https://render.com)
   - Sign up with GitHub

3. Create a New Web Service
   - Click "New +" -> "Web Service"
   - Connect your GitHub repository
   - Choose "Docker" as the environment

4. Configure the Service
   - Name: `notes-app` (or your preferred name)
   - Environment Variables (add these):
     - `SECRET_KEY`: Generate a secure random string
     - `DATABASE_URL`: (Optional) Add if using Postgres
   - Start Command: Leave empty (Dockerfile CMD is used)
   - Plan: Free or choose paid tier
   - Region: Choose closest to your users

5. Click "Create Web Service"

That's it! Render will:
- Use your Dockerfile to build the container
- Deploy the app
- Give you a `.onrender.com` URL

## Using PostgreSQL (Recommended for Production)

1. Create a Postgres Database
   - In Render Dashboard: "New +" -> "PostgreSQL"
   - Note the "Internal Database URL"

2. Update Web Service
   - Go to your web service
   - Add environment variable:
     - `DATABASE_URL`: Paste the Internal Database URL

## Local Testing

Test your Docker setup locally before deploying:

```bash
# Build the image
docker build -t notes-app .

# Run locally
docker run -e SECRET_KEY="dev-secret-key" -p 8080:8080 notes-app
```

Visit http://localhost:8080 to verify it works locally.

## Monitoring & Logs

- View logs: Render Dashboard -> Your Service -> Logs
- Monitor usage: Render Dashboard -> Your Service -> Metrics

## Troubleshooting

1. If build fails:
   - Check Render logs for specific errors
   - Verify Dockerfile builds locally
   - Ensure all dependencies are in requirements.txt

2. If app crashes:
   - Check environment variables are set
   - View logs in Render dashboard
   - Test locally with same configuration

3. Database issues:
   - Verify DATABASE_URL is set if using Postgres
   - Check database connection in logs
   - Ensure database is in same region as web service

Need help? Visit [Render Docs](https://render.com/docs) or create a support ticket.