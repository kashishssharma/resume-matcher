# Smart Resume Keyword Matcher (CLI)

A lightweight, CLI-based Python tool that compares a resume with a job description and provides:
- Keyword match score
- Semantic similarity score
- Missing and matching skills
- Resume improvement suggestions

Designed with clean architecture so the core logic can be reused in a future UI (e.g., Streamlit).

---

## Features
- CLI-first design
- TF-IDF based keyword extraction
- Generic keyword filtering (e.g., hiring, engineer)
- Keyword overlap scoring (explainable)
- Cosine similarity scoring (semantic accuracy)
- Clean separation between core logic and interface

---

## Project Structure
resume-matcher/
├── core/
│ ├── preprocess.py
│ ├── extractor.py
│ ├── similarity.py
│ ├── analyzer.py
│ └── constants.py
├── cli.py
├── resume.txt
├── jd.txt
├── requirements.txt
└── README.md


---

## How It Works
1. Extracts important keywords from resume and job description using TF-IDF
2. Filters generic role-based terms to improve relevance
3. Computes:
   - **Keyword Match Score** (overlap-based)
   - **Semantic Similarity Score** (cosine similarity)
4. Outputs missing skills and improvement suggestions

---

## Usage

### Install dependencies
pip install -r requirements.txt


### Run the CLI
python cli.py --resume resume.txt --jd jd.txt

### Sample Output
Keyword Match Score: 66%
Semantic Similarity Score: 72%

Missing Keywords:
- mongodb
- rest

Matching Keywords:
- python
- fastapi
- nlp
- backend

  
### Tech Stack

Python

scikit-learn

TF-IDF

Cosine Similarity
