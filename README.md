# Django-CRM — Duplicate Detection, Entity Matching & Data Quality Engine

[![CI](https://github.com/taran-dev4u/django-crm-lead-enrichment/actions/workflows/ci.yml/badge.svg)](https://github.com/taran-dev4u/django-crm-lead-enrichment/actions/workflows/ci.yml)
[![Upstream Repository](https://img.shields.io/badge/Django--CRM-1000%2B%20%E2%AD%90%20Open%20Source-orange?logo=github)](https://github.com/MicroPyramid/django-crm)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Production-grade entity matching, fuzzy duplicate detection, and automated record reconciliation engine for [Django-CRM](https://github.com/MicroPyramid/django-crm) (1,000+ ⭐).

---

## 🎯 Key Features

1. **Multi-Vector Duplicate Detection:** Matches leads, contacts, and accounts across normalized email addresses, E.164 phone formats, and corporate suffix pruning.
2. **Levenshtein Fuzzy Matching:** Configurable similarity scoring across fuzzy company names and contributor variations.
3. **Lossless Record Reconciliation:** Preserves primary master record identifiers while aggregating activities, tags, notes, and missing attributes.
4. **100% Deterministic Test Coverage:** Backed by automated unit test suites in pytest.

---

## 🏛️ Ecosystem Alignment

- **Upstream Repository:** [MicroPyramid/django-crm](https://github.com/MicroPyramid/django-crm)
- **Target Issue:** [#636 — Add Duplicate Detection and Merge](https://github.com/MicroPyramid/django-crm/issues/636)
- **Architecture:** Django REST Framework, Python, Pytest.

<!-- sync: 1787836791.8581748 -->
