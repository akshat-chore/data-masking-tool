# Data Masking / Anonymization Tool (version 7)

## Overview
This project is a proof-of-concept data masking tool designed to anonymize sensitive information while preserving data structure and referential integrity for testing purposes.

## Input
CSV dataset containing sensitive fields such as:
- Name
- Email
- Phone

## Masking Strategies Used
1. **Tokenization**
   - Used for names
   - Maintains a consistent token for the same input value

2. **Hashing (SHA-256)**
   - Used for email and phone numbers
   - Deterministic and irreversible

## Additional Masking Techniques
- Partial masking for phone numbers and emails
- Fake data substitution for improved test realism


## Referential Integrity
If the same sensitive value appears multiple times in the dataset,
it is always replaced with the same masked value.

## How to Run
```bash
pip install -r requirements.txt
python main.py
