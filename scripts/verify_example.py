"""Check the deliberately small, fictional case-study fixture with stdlib only."""

import json
from pathlib import Path


snapshot = json.loads(
    (Path(__file__).resolve().parent.parent / "data" / "synthetic-snapshot.json").read_text()
)

assert snapshot["schema_version"] == "1.0.0"
assert snapshot["snapshot_id"] == "snap_synthetic_showcase"
assert snapshot["counts"]["completed"] == 2

companies = snapshot["companies"]
assert len(companies) == 2
assert all(company["identity"]["cik"] is None for company in companies)
assert {company["identity"]["canonical_symbol"] for company in companies} == {"ALFA", "BRVO"}

def is_screened(company):
    return (
        company["scores"].get("total") is not None
        and bool(company["gate_results"])
        and company["classification"] != "unclassified"
    )


screened = [company for company in companies if is_screened(company)]
not_screened = [company for company in companies if not is_screened(company)]
assert len(screened) == 1 and screened[0]["classification"] == "investigate"
assert 20 <= screened[0]["scores"]["total"] <= 30
assert len(not_screened) == 1 and not_screened[0]["classification"] == "unclassified"
assert not not_screened[0]["gate_results"]
assert all(
    evidence["source"] == "synthetic-fixture"
    for company in companies
    for gate in company["gate_results"]
    for evidence in gate["evidence"]
)

print("Verified fictional example: 2 stored, 1 screened, 1 not screened.")
