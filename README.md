# Django-CRM — Enterprise Multi-Tenant CRM Engine & REST API Extensions

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.x%20%7C%20DRF-092E20.svg)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-blue.svg)](https://www.postgresql.org/)
[![Open Source](https://img.shields.io/badge/Open%20Source-1000%2B%20%E2%AD%90%20CRM-orange.svg)](https://github.com/MicroPyramid/Django-CRM)

---

## 📌 Executive Summary & Open Source Contributions

**Django-CRM** is a major open-source customer relationship management (CRM) platform built on Django and Django REST Framework (DRF), featuring lead tracking, account management, contact histories, sales opportunities, and case ticketing.

This repository features full-stack extensions, lead deduplication algorithms, and cloud attachment connectors developed by **Taran Mamidala**.

---

## 🚀 Key System Capabilities

- **Fuzzy Lead Deduplication:** String similarity and email domain matching preventing duplicate contact creations.
- **RESTful API Extensions:** Standardized DRF serializers with role-based permission gating.
- **Multi-Tenant Data Isolation:** Tenant-scoped querysets ensuring customer privacy.

---

## 📂 Repository Structure

```
django-crm-lead-enrichment/
├── src/crm_enrichment/              # Duplicate detection algorithms and API serializers
├── tests/                           # Unit tests for multi-tenant lead management
└── README.md                        # Documentation
```

---

## 👨‍💻 Author & Contributor
- **Author:** Taran Mamidala
- **Upstream Repository:** [MicroPyramid/Django-CRM](https://github.com/MicroPyramid/Django-CRM)
