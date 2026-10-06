# AI Resume Analyzer

A full-stack AI/NLP project that analyzes a resume against a job description and generates an ATS-style score, matching skills, missing skills, detected resume sections, and improvement suggestions.

## Features
- PDF and DOCX resume upload
- Resume text extraction
- Skill extraction using a technical-skill dictionary
- TF-IDF + cosine similarity for resume/job-description similarity
- ATS-style score
- Matching and missing skills
- Resume section detection
- Improvement suggestions
- SQLite database for analysis history
- Responsive frontend
- Frontend and backend in one GitHub repository

## Tech Stack
Frontend: HTML5, CSS3, JavaScript
Backend: Python, Flask, REST API
AI/NLP: TF-IDF, cosine similarity, keyword/skill extraction, rule-based section detection
Database: SQLite

## Project Structure
```text
AI-Resume-Analyzer/
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── backend/
│   ├── app.py
│   ├── resume_parser.py
│   ├── matcher.py
│   └── database.py
├── uploads/
│   └── .gitkeep
├── requirements.txt
├── .gitignore
└── README.md
```

## How It Works
1. User uploads a PDF/DOCX resume.
2. User pastes a job description.
3. Flask receives the request through `/analyze`.
4. The resume parser extracts text.
5. The matcher detects technical skills.
6. TF-IDF converts resume and job-description text into vectors.
7. Cosine similarity measures textual similarity.
8. Resume sections are detected.
9. An ATS-style score is calculated.

### Score Formula
```text
ATS Score = 50% Skill Match + 30% TF-IDF Similarity + 20% Resume Structure
```
This is an educational ATS-style score, not an official score from any ATS vendor.

## Installation
### Windows PowerShell
```powershell
git clone https://github.com/YOUR-USERNAME/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python backend/app.py
```
If PowerShell blocks activation, use:
```powershell
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe backend\app.py
```
Open http://127.0.0.1:5000

## API
`GET /health` checks the server.
`POST /analyze` accepts multipart form data with `resume` and `job_description`.

## Testing Checklist
- Homepage loads
- Resume upload works
- Job description input works
- PDF analysis works
- DOCX analysis works
- Matching skills appear
- Missing skills appear
- ATS score appears
- Suggestions appear
- Invalid file is rejected
- File over 5 MB is rejected
- `/health` returns OK

## Future Improvements
- Login and user dashboard
- spaCy-based NLP
- Job recommendations
- Multiple resume comparison
- Admin analytics dashboard
- Cloud deployment
- PostgreSQL
- Authentication and encrypted file storage

## Author
AIML / Computer Science Engineering student project demonstrating full-stack development, NLP and machine learning concepts.
