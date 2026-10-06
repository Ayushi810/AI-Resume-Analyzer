import sqlite3
from pathlib import Path
DB_PATH=Path(__file__).resolve().parent/"resume_analyzer.db"

def init_db():
    connection=sqlite3.connect(DB_PATH)
    connection.execute("""CREATE TABLE IF NOT EXISTS analyses (id INTEGER PRIMARY KEY AUTOINCREMENT, filename TEXT NOT NULL, ats_score REAL NOT NULL, matching_skills TEXT, missing_skills TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
    connection.commit(); connection.close()

def save_analysis(filename,ats_score,matching_skills,missing_skills):
    connection=sqlite3.connect(DB_PATH)
    connection.execute("INSERT INTO analyses (filename,ats_score,matching_skills,missing_skills) VALUES (?,?,?,?)",(filename,ats_score,", ".join(matching_skills),", ".join(missing_skills)))
    connection.commit(); connection.close()
init_db()
