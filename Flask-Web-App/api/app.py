from website import create_app

# Expose the Flask WSGI app for the Vercel Python builder.
# Vercel will import this module and use the `app` WSGI callable.
app = create_app()
