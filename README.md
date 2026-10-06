# AI Resume Analyzer

An AI/NLP-based full-stack web application that analyzes a candidate's resume against a job description and generates an ATS-style compatibility score.

The application identifies matching skills, missing skills, resume sections, and provides suggestions to improve the resume for a particular job role.

---

## 🚀 Features

- Upload Resume in PDF or DOCX format
- Paste Job Description
- Automatic Resume Text Extraction
- Technical Skill Detection
- Resume vs Job Description Matching
- ATS-Style Compatibility Score
- Matching Skills Detection
- Missing Skills Detection
- Resume Section Detection
- Personalized Resume Improvement Suggestions
- SQLite Database for storing analysis results
- Responsive Web Interface
- Frontend and Backend in a Single Repository

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask
- REST API

### AI / NLP
- TF-IDF
- Cosine Similarity
- Keyword Matching
- Skill Extraction
- Text Processing

### Database
- SQLite

### Libraries
- Flask
- PyPDF
- python-docx
- Scikit-learn
- Werkzeug

---

## 📂 Project Structure

```text
AI-Resume-Analyzer/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── backend/
│   ├── app.py
│   ├── resume_parser.py
│   ├── matcher.py
│   └── database.py
│
├── uploads/
│   └── .gitkeep
│
├── requirements.txt
├── .gitignore
├── README.md
└── LICENSE
