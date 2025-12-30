def compute_similarity(resume_keywords: list, jd_keywords: list) -> dict:
    """
    Compare resume and JD keywords.
    """
    resume_set = set(resume_keywords)
    jd_set = set(jd_keywords)

    matching = resume_set.intersection(jd_set)
    missing = jd_set.difference(resume_set)

    match_score = int((len(matching) / len(jd_set)) * 100) if jd_set else 0

    return {
        "match_score": match_score,
        "matching_keywords": sorted(list(matching)),
        "missing_keywords": sorted(list(missing)),
    }

