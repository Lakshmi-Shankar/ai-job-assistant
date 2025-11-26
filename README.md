# **AI Job Assistant – Flask Backend**

A lightweight Flask-based backend that generates **AI-powered job role recommendations** using the **Google Gemini API**.
Given a list of skills, the API returns 5 best-fit tech roles with match percentage and reasoning.

---

## **Features**

* Accepts a list of skills and returns:

  * Recommended job titles
  * Explanation for each match
  * Match percentage
* Uses **Gemini 2.5 Flash** for fast response.
* Clean JSON output for easy frontend integration.
* CORS enabled (ready for React/Vite/Next.js frontend).
* Fully modular and simple to deploy.

---

## **Tech Stack**

* **Python**
* **Flask**
* **Google Gemini API (Generative AI)**
* **Flask-CORS**
* **dotenv**
* **JSON + Regex parsing**

---

## Live API
Base URL: https://ai-job-assistant-kj06.onrender.com

## **API Endpoints**

### **1. GET /**

Check server status.

**Response:**

```json
{
  "message": "AI Job Recommendation API is running",
  "usage": "POST /recommend with JSON { 'skills': ['React', 'Node.js', 'Python'] }"
}
```

---

### **2. POST /recommend**

Send a list of skills to get job recommendations.

**Request Body Example:**

```json
{
  "skills": ["Python", "SQL", "Machine Learning"]
}
```

**Response Example:**

```json
[
  {
    "job_title": "Machine Learning Engineer",
    "reason": "Strong Python and ML foundations suitable for model development.",
    "match_percentage": 85
  },
  {
    "job_title": "Data Analyst",
    "reason": "SQL and analytical thinking strongly align with the role.",
    "match_percentage": 80
  }
]
```

If JSON is missing or invalid:

```json
{
  "content": "Please provide a non-empty list of skills."
}
```

---

## **Project Structure**

```
ai-job-assistant/
│── app.py  
│── .env  
│── requirements.txt  
│── README.md  
```

---

## **Setup Instructions**

### **1. Clone the repository**

```bash
git clone https://github.com/Lakshmi-Shankar/ai-job-assistant
cd ai-job-assistant
```

### **2. Install dependencies**

```bash
pip install -r requirements.txt
```

### **3. Add your Gemini API key**

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_api_key_here
```

### **4. Run the server**

```bash
python app.py
```

Server starts on:

```
http://localhost:5000
```

---

## **How the AI works**

The backend sends a structured prompt to Gemini LLM:

* It analyzes the provided skills
* Maps them to common tech roles
* Assigns match percentages
* Returns a clean JSON array

You can easily connect a frontend to display recommendations.

---

## **Future Enhancements**

* Resume upload + skill extraction
* Detailed job description matching
* Weighted scoring based on experience
* Save user history

---
