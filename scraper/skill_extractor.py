def extract_skills(text):
    text = text.lower()

    skill_map = {
        "python": ["python"],
        "sql": ["sql"],
        "excel": ["excel"],
        "power bi": ["power bi", "powerbi"],
        "tableau": ["tableau"],
        "machine learning": ["machine learning", "ml"],
        "deep learning": ["deep learning"],
        "nlp": ["nlp"],
        "statistics": ["statistics", "statistical"],
        "aws": ["aws"],
        "pandas": ["pandas"],
        "numpy": ["numpy"],
        "data analysis": ["data analysis", "analysis"],
    }

    found_skills = set()

    for skill, keywords in skill_map.items():
        for word in keywords:
            if word in text:
                found_skills.add(skill)

    return list(found_skills)