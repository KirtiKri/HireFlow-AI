"""Conservative passage-level evidence checks, not a competency assessment.

Only explicit, non-negated mentions count as *documented mentions*. This is
intentionally not a semantic inference engine; ambiguous text needs human review.
"""
import re
from app.tools import SKILL_ALIASES

_NEGATED_CONTEXT = re.compile(
    r"\b(?:no|never|not|without|lack|lacking|unfamiliar\s+with|"
    r"haven.t|hasn.t|don.t|doesn.t|cannot|can.t|"
    r"want\s+to\s+learn|wants\s+to\s+learn|"
    r"currently\s+learning|still\s+learning|learning|"
    r"beginner\s+in|no\s+experience\s+with)\b", re.I)
_NEGATED_AFTER = re.compile(
    r"^\s*(?::|[-–—])?\s*(?:no|not|never|none|without|"
    r"beginner|learning|unfamiliar|lack|lacking)\b", re.I)
# A contrast marker starts a new clause; a negation in one clause should not
# automatically invalidate an unrelated positive claim in the next.
_CLAUSE_SPLIT = re.compile(r"[\n.!?;]+|\s*,\s*(?=(?:but|however|although)\b)|\s+\b(?:but|however|although)\b\s*", re.I)

def skill_supported(skill: str, passage: str) -> bool:
    aliases = SKILL_ALIASES.get(skill.lower(), [skill.lower()])
    for clause in _CLAUSE_SPLIT.split(passage):
        for alias in aliases:
            for match in re.finditer(r"(?<!\w)" + re.escape(alias) + r"(?!\w)", clause, re.I):
                before = clause[max(0, match.start() - 65):match.start()]
                after = clause[match.end():match.end() + 35]
                if not _NEGATED_CONTEXT.search(before) and not _NEGATED_AFTER.search(after):
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
