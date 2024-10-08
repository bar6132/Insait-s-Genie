import google.generativeai as genai
import json
import logging
import os
logger = logging.getLogger(__name__)

gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)


def get_gemini_answer(question):
    try:
        # Create the prompt using the question
        prompt = f"""
        Answer the following Question: {question}

        Instructions:
        - Make the Answer Short and accurate.
        - Limit the Answer to 1 Line.
        """

        # Define the generation configuration
        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 50,
            "response_mime_type": "application/json",
        }

        # Initialize the GenerativeModel for Gemini AI
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
        )

        # Generate the content based on the question
        response = model.generate_content(prompt)

        # Extract the answer from the response
        raw_answer = response.candidates[0].content.parts[0].text.strip()

        # Remove unnecessary escaping
        parsed_answer = json.loads(raw_answer)  # Assuming the response is a JSON string
        answer = parsed_answer["answer"]  # Extract the 'answer' field

        logging.info(f"Generated answer: {answer}")
        return {"question": question, "answer": answer}

    except Exception as e:
        logging.error(f"Error generating answer: {str(e)}")
        return {"question": question, "answer": "Error generating answer"}
