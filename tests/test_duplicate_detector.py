import pytest
from django_crm_enrichment.duplicate_detector import DuplicateDetector

def test_exact_email_match():
    detector = DuplicateDetector()
    record = {"id": 1, "name": "Alice Smith", "email": "alice@example.com", "phone": "123-456"}
    candidates = [
        {"id": 2, "name": "Alice S.", "email": "ALICE@example.com", "phone": "999-000"},
        {"id": 3, "name": "Bob Jones", "email": "bob@example.com", "phone": "123-456"}
    ]
    dups = detector.find_duplicates(record, candidates)
    assert len(dups) == 2
    assert any(d["candidate_id"] == 2 and "exact_email_match" in d["reasons"] for d in dups)
    assert any(d["candidate_id"] == 3 and "exact_phone_match" in d["reasons"] for d in dups)

def test_fuzzy_name_and_company_matching():
    detector = DuplicateDetector(fuzzy_threshold=0.8)
    record = {"id": 1, "name": "Acme Innovations", "company": "Acme Corp Inc"}
    candidates = [
        {"id": 2, "name": "Acme Innovation", "company": "Acme Corporation"},
        {"id": 3, "name": "Zenith Global", "company": "Zenith LLC"}
    ]
    dups = detector.find_duplicates(record, candidates)
    assert len(dups) == 1
    assert dups[0]["candidate_id"] == 2

def test_phone_normalization():
    detector = DuplicateDetector()
    assert detector.normalize_phone("+1 (555) 019-2834") == "+15550192834"
    assert detector.normalize_phone("555.019.2834") == "5550192834"

def test_merge_records():
    detector = DuplicateDetector()
    master = {"id": 1, "name": "Master Lead", "email": "master@example.com", "phone": None, "tags": ["lead", "enterprise"]}
    duplicate = {"id": 2, "name": "Old Lead", "email": "old@example.com", "phone": "+15550192834", "city": "San Francisco", "tags": ["tier1", "lead"]}
    
    merged = detector.merge_records(master, duplicate)
    assert merged["id"] == 1
    assert merged["name"] == "Master Lead"
    assert merged["email"] == "master@example.com"
    assert merged["phone"] == "+15550192834"
    assert merged["city"] == "San Francisco"
    assert set(merged["tags"]) == {"lead", "enterprise", "tier1"}
