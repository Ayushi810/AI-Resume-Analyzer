import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

SKILLS=["python","java","c++","javascript","typescript","html","css","react","angular","node.js","express","flask","django","sql","mysql","postgresql","mongodb","git","github","docker","aws","azure","machine learning","deep learning","artificial intelligence","nlp","natural language processing","tensorflow","keras","pytorch","scikit-learn","pandas","numpy","streamlit","data analysis","data visualization","power bi","excel","rest api","api","linux","cloud","agile","scrum"]
SECTION_PATTERNS={"Contact":[r"\bemail\b",r"\bphone\b",r"\bmobile\b",r"\blinkedin\b"],"Summary":[r"\bsummary\b",r"\bobjective\b",r"\bprofile\b"],"Education":[r"\beducation\b",r"\bdegree\b",r"\bbtech\b",r"\bbachelor\b"],"Skills":[r"\bskills\b",r"\btechnical skills\b"],"Projects":[r"\bprojects\b",r"\bproject\b"],"Experience":[r"\bexperience\b",r"\binternship\b",r"\bwork experience\b"],"Certifications":[r"\bcertifications?\b",r"\bcertificate\b"]}

def normalize(text): return re.sub(r"\s+"," ",text.lower()).strip()

def find_skills(text):
    normalized=normalize(text); found=[]
    for skill in SKILLS:
        pattern=r"(?<![a-z0-9])"+re.escape(skill.lower())+r"(?![a-z0-9])"
        if re.search(pattern,normalized): found.append(skill)
    return found

def section_detection(text):
    normalized=normalize(text)
    return {section:any(re.search(pattern,normalized) for pattern in patterns) for section,patterns in SECTION_PATTERNS.items()}

def similarity_score(resume_text,job_description):
    vectorizer=TfidfVectorizer(stop_words="english",ngram_range=(1,2))
    matrix=vectorizer.fit_transform([resume_text,job_description])
    return round(float(cosine_similarity(matrix[0:1],matrix[1:2])[0][0])*100,2)

def analyze_resume(resume_text,job_description):
    resume_skills=find_skills(resume_text); job_skills=find_skills(job_description)
    matching=sorted(set(resume_skills)&set(job_skills)); missing=sorted(set(job_skills)-set(resume_skills))
    keyword_score=(len(matching)/len(job_skills)*100) if job_skills else 70
    similarity=similarity_score(resume_text,job_description)
    sections=section_detection(resume_text); section_score=sum(sections.values())/len(sections)*100
    ats_score=round((keyword_score*.50)+(similarity*.30)+(section_score*.20),2); ats_score=min(100,max(0,ats_score))
    suggestions=[]
    if missing: suggestions.append("If you genuinely have these skills, add them clearly to your Skills or Projects section: "+", ".join(missing[:8])+".")
    if not sections["Projects"]: suggestions.append("Add a dedicated Projects section with measurable outcomes and technologies used.")
    if not sections["Experience"]: suggestions.append("Add internship, training, freelance, or relevant experience if applicable.")
    if not sections["Education"]: suggestions.append("Add a clear Education section with degree, university and graduation year.")
    if not sections["Contact"]: suggestions.append("Keep professional contact details such as email, phone and LinkedIn easy to find.")
    if similarity<35: suggestions.append("Rewrite some resume bullets to reflect the terminology and responsibilities in the job description.")
    if not suggestions: suggestions.append("Good structure detected. Focus on measurable achievements and keep the resume concise.")
    if ats_score>=80: message="Strong match. Your resume is well aligned with this job description."
    elif ats_score>=60: message="Good starting point. Add relevant missing keywords and improve alignment with the job description."
    else: message="The match is currently low. Tailor your resume to the role before applying."
    return {"ats_score":ats_score,"score_message":message,"matching_skills":matching,"missing_skills":missing,"sections":sections,"suggestions":suggestions}
