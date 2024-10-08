import logging
from extensions import db
from psycopg2 import sql, connect
import os

# Configure logging
logger = logging.getLogger(__name__)


# Define the QA model
class QA(db.Model):
    __tablename__ = 'qa'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(512), nullable=False)
    answer = db.Column(db.Text, nullable=False)


# Repository for handling database operations related to QA
class QARepository:
    def __init__(self, session):
        self.session = session

    def add_question(self, question, answer):
        try:
            qa = QA(question=question, answer=answer)
            self.session.add(qa)
            self.session.commit()
            logger.info("Question and answer added to the database.")
        except Exception as e:
            logger.error(f"Error adding QA: {e}")
            self.session.rollback()


# Function to check and create the database (optional)
def create_database():
    try:
        conn = connect(
            dbname='postgres',  # Connect to default 'postgres' database
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
        )
        conn.autocommit = True
        cursor = conn.cursor()

        # Check if the database exists
        cursor.execute(sql.SQL("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s"), [os.getenv('DB_NAME')])
        exists = cursor.fetchone()
        if not exists:
            cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(os.getenv('DB_NAME'))))
            logger.info(f"Database {os.getenv('DB_NAME')} created successfully.")
        else:
            logger.info(f"Database {os.getenv('DB_NAME')} already exists.")

        cursor.close()
        conn.close()
    except Exception as e:
        logger.error(f"An error occurred while creating the database: {e}")


# Function to create tables
def create_tables():
    try:
        logger.info("Creating tables...")
        db.create_all()
        logger.info("Tables created successfully (or already exist).")
    except Exception as e:
        logger.error(f"An error occurred while creating tables: {e}")
