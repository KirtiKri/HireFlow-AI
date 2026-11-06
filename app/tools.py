import re

# Demo vocabulary; extend only with documented skill aliases.
SKILL_ALIASES = {
    "python": ["python"],
    "sql": ["sql", "postgresql", "mysql", "sqlite"],
    "git": ["git", "github", "gitlab"],
    "rest api": ["rest api", "restful api", "rest apis"],
    "pandas": ["pandas"],
    "numpy": ["numpy"],
    "machine learning": ["machine learning"],
    "docker": ["docker"],
    "java": ["java"],
    "javascript": ["javascript"],
    "excel": ["excel"],
    "power bi": ["power bi", "powerbi"],
    "communication": ["communication"],
}

def find_skills(text: str) -> list[str]:
    found = []
    for skill, aliases in SKILL_ALIASES.items():
        if any(re.search(r"(?<!\w)" + re.escape(a) + r"(?!\w)", text, re.I) for a in aliases):
            found.append(skill)
    return found

def evidence_for(text: str, skills: list[str]) -> dict[str, str]:
    sentences = [s.strip() for s in re.split(r"[\n.!?]+", text) if s.strip()]
    result = {}
    for skill in skills:
        for sentence in sentences:
            if any(re.search(r"(?<!\w)" + re.escape(alias) + r"(?!\w)", sentence, re.I)
                   for alias in SKILL_ALIASES.get(skill, [skill])):
                result[skill] = sentence[:240]
                break
    return result
