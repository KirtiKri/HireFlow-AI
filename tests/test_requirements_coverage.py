from app.tools import find_skills, evidence_for
from app.evidence_report import build_evidence_rows

JOB = '''We are seeking a Junior Data Analyst with proficiency in Python, SQL,
pandas, Excel, and dashboard development. Candidates should have experience
cleaning datasets, analyzing business metrics, and communicating insights.
Experience with Power BI, cloud platforms (AWS or Azure), and ETL pipelines is desirable.'''
RESUME = '''Python: pandas, NumPy; data cleaning, dashboard design.
SQL queries and Excel PivotTables.'''

def test_requirement_coverage():
    required = find_skills(JOB)
    for skill in ('python', 'sql', 'pandas', 'excel', 'power bi', 'aws', 'azure', 'etl'):
        assert skill in required, (skill, required)
    observed = find_skills(RESUME)
    supported = sorted(set(required) & set(observed))
    missing = sorted(set(required) - set(observed))
    review = {'supported_skills': supported, 'missing_skills': missing,
              'evidence': evidence_for(RESUME, observed)}
    rows = build_evidence_rows(review)
    findings = {r['Requirement']: r['Finding'] for r in rows}
    for skill in ('power bi', 'aws', 'azure', 'etl'):
        assert findings[skill] == 'Not evidenced in saved review'
