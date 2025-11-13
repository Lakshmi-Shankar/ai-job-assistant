from flask import Flask, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
import os
import json
import re
from flask_cors import CORS 

# Load environment variables
load_dotenv()

# Get API key from .env
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("Missing GEMINI_API_KEY in .env file")

# Configure Gemini API key
genai.configure(api_key=API_KEY)

MODEL_NAME = "models/gemini-2.5-flash"

app = Flask(__name__)
CORS(app)

def get_job_recommendations(skills):
    prompt = f"""
    You are an expert tech career advisor.
    Based only on the following skills, recommend 5 best-fit tech job roles.
    For each role, include:
    - job_title
    - reason
    - match_percentage (integer between 0-100)

    Skills: {', '.join(skills)}

    Output only valid JSON array of objects with keys:
    job_title, reason, match_percentage
    """

    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(prompt)
        content = response.text.strip()

        # Clean JSON formatting
        content = re.sub(r"^```json|```$", "", content.strip(), flags=re.MULTILINE).strip()

        try:
            return json.loads(content)
        except json.JSONDecodeError:
            return {"error": "Model response not valid JSON", "raw": content}

    except Exception as e:
        return {"error": str(e)}


@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()

    if not data or "skills" not in data:
        return jsonify({"error": "Missing 'skills' in request body"}), 400

    skills = data["skills"]

    if not isinstance(skills, list) or not skills:
        return jsonify({"error": "'skills' must be a non-empty list"}), 400

    recommendations = get_job_recommendations(skills)
    return jsonify(recommendations)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "AI Job Recommendation API is running",
        "usage": "POST /recommend with JSON { 'skills': ['React', 'Node.js', 'Python'] }"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
