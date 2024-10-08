
# AI Question-Answer API with Flask and PostgreSQL

## Overview
This project is a Flask-based application designed to handle user-submitted questions, send the questions to an AI service (such as OpenAI or Gemini AI), and return answers. The system stores both the questions and answers in a PostgreSQL database. The Flask server and PostgreSQL database are Dockerized, and database migrations are managed using Alembic. The project also includes automated tests to verify that the /ask endpoint works as expected.


## Features
- **Ask a Question:** Users can send questions to the /ask endpoint, and the system will return an AI-generated answer.
- **AI Integration:** The application fetches the latest news based on user preferences and sends the most interesting news to users.
- **Persistent Storage :** Questions and answers are stored in a PostgreSQL database..
- **Dockerized Services:** The Flask app and PostgreSQL database are containerized using Docker and managed via Docker Compose.
- **Database Migrations:** Alembic is used to handle database migrations.
- **Testing:** Includes test to verify the functionality of the /ask endpoint using pytest.


## Technologies Used
- **Flask:** For creating the main application and handling requests.
- **SQLAlchemy:** For ORM and database interactions.
- **PostgreSQL:** To store the questions and answers.
- **Alembic:** For database migrations.
- **Docker & Docker Compose:** For containerization of the services.
- **pytest:** For testing the application.
- **Gemini:** For AI-based answers.


## Project Structure
```
/project-root
    ├── app.py                 # Main Flask app
    ├── models.py              # Database models
    ├── extensions.py          # Extensions setup (e.g., SQLAlchemy)
    ├── routes.py              # routes setup ('/ask')
    ├── services.py            # gemini setup 
    ├── config.py              # Database config setup 
    ├── migrations/            # Alembic migration scripts
    ├── docker-compose.yml     # Docker Compose setup
    ├── Dockerfile             # Dockerfile for the Flask app
    ├── README.md              # Project documentation
    ├── tests/
    │   ├── test_app.py        # Test files using pytest
    └── .env                   # Environment variables (if not using Docker Compose for env)

## Setup and Installation
1. **Clone the repository:**
    ```bash 
	git clone https://https://github.com/bar6132/Insait-s-Backend-internship .
    ```
2. **Build and run the services using Docker Compose:**
    ```bash
    docker-compose up --build
    ```


## Usage
**Send a Question:** Endpoint: POST /ask 
                        {
                        "question": "What is Python?"
                        }. 

**Get a Answer:** 
                {
                  "question": "What is Python?",
                  "answer": "Python is a versatile and powerful programming language."
                }


## Testing
- **Testing:** "docker-compose exec web pytest".

