from website import create_app
import os

app = create_app()

if __name__ == '__main__':
    # Respect FLASK_DEBUG env var; default to False in production
    debug = os.environ.get('FLASK_DEBUG', '0') == '1'
    # Bind to 0.0.0.0 so the server is accessible inside containers
    app.run(host='0.0.0.0', debug=debug)
