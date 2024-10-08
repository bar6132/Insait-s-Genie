from flask import Blueprint, request, jsonify
from services import get_gemini_answer
from models import QA
from extensions import db  # Import db from extensions
import logging

# Configure logging
logger = logging.getLogger(__name__)

# Create a blueprint for the routes
ask_bp = Blueprint('ask_bp', __name__)


@ask_bp.route('/ask', methods=['POST'])
async def ask_question():
    data = request.get_json()

    if 'question' not in data:
        return jsonify({"error": "Question is required"}), 400

    question = data['question']

    try:
        # Get answer from Gemini AI
        answer = get_gemini_answer(question)

        # Store the question and answer in the database
        qa = QA(question=question, answer=answer['answer'])
        db.session.add(qa)
        db.session.commit()

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(answer)

