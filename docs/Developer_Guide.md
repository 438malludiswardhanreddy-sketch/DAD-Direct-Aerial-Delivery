# DAD Developer Setup Guide

## 1. Local Development Setup
1.  **Clone Repository**:
    ```bash
    git clone https://github.com/438malludiswardhanreddy-sketch/DAD-Direct-Aerial-Delivery.git
    cd DAD-Direct-Aerial-Delivery
    ```
2.  **Environment Setup**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

## 2. Directory Layout & Module Adding
*   Add new range calculation filters under `sensor_fusion/`.
*   Add autonomous path adjustments and meteorological limit overrides under `autonomous/`.
*   Add API endpoints under `backend/routes/`.

## 3. Running Unit Tests
Validate codebase alignments:
```bash
python testing/test_suite.py
```
Ensure all tests print `OK`.
