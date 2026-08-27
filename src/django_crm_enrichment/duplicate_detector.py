"""
Django-CRM Duplicate Detection and Record Merge Engine.
Implements fuzzy matching, email/phone normalization, and M2M relation reconciliation.
"""
from typing import Dict, List, Any, Optional, Set
import re
import difflib

class DuplicateDetector:
    """Detects duplicate contacts, leads, and accounts using exact and fuzzy matching rules."""

    def __init__(self, fuzzy_threshold: float = 0.85):
        self.fuzzy_threshold = fuzzy_threshold

    @staticmethod
    def normalize_phone(phone: Optional[str]) -> str:
        if not phone:
            return ""
        # Strip all non-digit characters except leading +
        digits = re.sub(r"[^\d+]", "", phone.strip())
        if digits.startswith("+"):
            return "+" + re.sub(r"[^\d]", "", digits[1:])
        return digits

    @staticmethod
    def normalize_email(email: Optional[str]) -> str:
        if not email:
            return ""
        return email.strip().lower()

    @staticmethod
    def normalize_company(company: Optional[str]) -> str:
        if not company:
            return ""
        comp = company.strip().lower()
        # Remove common corporate suffixes for matching
        suffixes = [" inc", " inc.", " llc", " corp", " corp.", " ltd", " ltd.", " gmbh", " co", " co."]
        for s in suffixes:
            if comp.endswith(s):
                comp = comp[:-len(s)].strip()
        return comp

    def calculate_similarity(self, s1: str, s2: str) -> float:
        if not s1 or not s2:
            return 0.0
        return difflib.SequenceMatcher(None, s1.lower(), s2.lower()).ratio()

    def find_duplicates(self, record: Dict[str, Any], candidates: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        duplicates = []
        rec_email = self.normalize_email(record.get("email"))
        rec_phone = self.normalize_phone(record.get("phone"))
        rec_company = self.normalize_company(record.get("company"))
        rec_name = (record.get("name") or "").strip().lower()

        for cand in candidates:
            if cand.get("id") == record.get("id"):
                continue

            match_reasons = []
            cand_email = self.normalize_email(cand.get("email"))
            cand_phone = self.normalize_phone(cand.get("phone"))
            cand_company = self.normalize_company(cand.get("company"))
            cand_name = (cand.get("name") or "").strip().lower()

            if rec_email and cand_email and rec_email == cand_email:
                match_reasons.append("exact_email_match")

            if rec_phone and cand_phone and rec_phone == cand_phone:
                match_reasons.append("exact_phone_match")

            if rec_name and cand_name:
                name_sim = self.calculate_similarity(rec_name, cand_name)
                if name_sim >= self.fuzzy_threshold:
                    match_reasons.append(f"fuzzy_name_match_{name_sim:.2f}")

            if rec_company and cand_company:
                comp_sim = self.calculate_similarity(rec_company, cand_company)
                if comp_sim >= self.fuzzy_threshold:
                    match_reasons.append(f"fuzzy_company_match_{comp_sim:.2f}")

            if match_reasons:
                duplicates.append({
                    "candidate_id": cand.get("id"),
                    "candidate": cand,
                    "reasons": match_reasons,
                    "confidence": "HIGH" if len(match_reasons) > 1 or "exact_email_match" in match_reasons else "MEDIUM"
                })

        return duplicates

    def merge_records(self, master: Dict[str, Any], duplicate: Dict[str, Any]) -> Dict[str, Any]:
        """Merges duplicate fields into master without overwriting populated master attributes."""
        merged = dict(master)
        for k, v in duplicate.items():
            if k == "id":
                continue
            if k not in merged or merged[k] is None or merged[k] == "":
                merged[k] = v

        # Merge tags/lists
        for list_key in ["tags", "assigned_to", "activities"]:
            if list_key in master or list_key in duplicate:
                m_list = master.get(list_key) or []
                d_list = duplicate.get(list_key) or []
                merged[list_key] = list(dict.fromkeys(m_list + d_list))

        return merged
