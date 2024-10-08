from flask import Flask
from dotenv import load_dotenv
import logging
from extensions import db
import os
from models import QA
from routes import ask_bp
# Load environment variables

load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configure the database
app.config.from_object('config.Config')

# Initialize SQLAlchemy
db.init_app(app)  # Initialize the db with the app


# Register the routes blueprint
app.register_blueprint(ask_bp)

# Create the database and tables if they don't exist
with app.app_context():
    from models import create_database, create_tables
    create_database()
    create_tables()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
