"""Conservative, deterministic evidence checks (not a hiring decision)."""
import re
from app.tools import SKILL_ALIASES

NEGATIONS = re.compile(r"\b(no|never|not|without|lack|lacking|unfamiliar with|want to learn|learning)\b", re.I)

def skill_supported(skill: str, passage: str) -> bool:
    aliases = SKILL_ALIASES.get(skill.lower(), [skill.lower()])
    for alias in aliases:
        match = re.search(r"(?<!\w)" + re.escape(alias) + r"(?!\w)", passage, re.I)
        if match:
            preceding = passage[max(0, match.start() - 55):match.start()]
            # A cautious heuristic. False negatives are possible and require human review.
            if not NEGATIONS.search(preceding):
                return True
    return False

def verified_evidence(text: str, skills: list[str]) -> dict[str, str]:
    passages = [p.strip() for p in re.split(r"[\n.!?]+", text) if p.strip()]
    evidence = {}
    for skill in skills:
        for passage in passages:
            if skill_supported(skill, passage):
                evidence[skill] = passage[:300]
                break
    return evidence
