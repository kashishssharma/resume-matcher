import argparse
from core.analyzer import analyze_resume

def read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def main():
    parser = argparse.ArgumentParser(description="Smart Resume Keyword Matcher")
    parser.add_argument("--resume", required=True, help="Path to resume text file")
    parser.add_argument("--jd", required=True, help="Path to job description text file")

    args = parser.parse_args()

    resume_text = read_file(args.resume)
    jd_text = read_file(args.jd)

    result = analyze_resume(resume_text, jd_text)

    print(f"\nMatch Score: {result['match_score']}%\n")

    print("Missing Keywords:")
    for kw in result["missing_keywords"]:
        print(f"- {kw}")

    print("\nMatching Keywords:")
    for kw in result["matching_keywords"]:
        print(f"- {kw}")

    print("\nSuggestions:")
    for s in result["suggestions"]:
        print(f"- {s}")

if __name__ == "__main__":
    main()
