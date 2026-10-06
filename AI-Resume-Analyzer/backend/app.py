from pathlib import Path
import uuid
from flask import Flask, jsonify, request, send_from_directory
from werkzeug.utils import secure_filename
from resume_parser import extract_text
from matcher import analyze_resume
from database import save_analysis

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"
UPLOAD_DIR = BASE_DIR / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)
ALLOWED_EXTENSIONS = {"pdf", "docx"}
MAX_FILE_SIZE = 5 * 1024 * 1024
app = Flask(__name__, static_folder=str(FRONTEND_DIR), static_url_path="")
app.config["MAX_CONTENT_LENGTH"] = MAX_FILE_SIZE

def allowed_file(filename):
    return "." in filename and filename.rsplit(".",1)[1].lower() in ALLOWED_EXTENSIONS

@app.get("/")
def home(): return send_from_directory(FRONTEND_DIR, "index.html")

@app.get("/health")
def health(): return jsonify({"status":"ok","message":"AI Resume Analyzer API is running"})

@app.post("/analyze")
def analyze():
    if "resume" not in request.files: return jsonify({"error":"Resume file is required."}),400
    file=request.files["resume"]; job_description=request.form.get("job_description","").strip()
    if not file.filename: return jsonify({"error":"Please select a resume file."}),400
    if not allowed_file(file.filename): return jsonify({"error":"Only PDF and DOCX files are supported."}),400
    if not job_description: return jsonify({"error":"Job description is required."}),400
    filename=secure_filename(file.filename); saved_name=f"{uuid.uuid4().hex}_{filename}"; file_path=UPLOAD_DIR/saved_name; file.save(file_path)
    try:
        resume_text=extract_text(file_path)
        if len(resume_text.strip())<80: return jsonify({"error":"Could not extract enough text from the resume. Try a text-based PDF/DOCX."}),400
        result=analyze_resume(resume_text,job_description)
        save_analysis(filename,result["ats_score"],result["matching_skills"],result["missing_skills"])
        return jsonify(result)
    except Exception as exc: return jsonify({"error":f"Analysis error: {str(exc)}"}),500
    finally:
        if file_path.exists(): file_path.unlink()

@app.errorhandler(413)
def too_large(_error): return jsonify({"error":"File is too large. Maximum size is 5 MB."}),413

if __name__ == "__main__": app.run(debug=True,host="127.0.0.1",port=5000)
