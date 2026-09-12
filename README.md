# Serverless Student Result Management System

A Cloud Computing academic project demonstrating a student-result application designed with a serverless-ready architecture.

## Key Features
- Add, view, and delete students
- Add subject marks
- Calculate grades and percentage
- Determine pass/fail status
- View individual and all results
- SQLite local development mode
- AWS Lambda-ready health function
- Serverless Framework configuration
- Automated test
- Fully executable from terminal

## Requirements
- Python 3.9+
- pip
- Terminal/Command Prompt
- Optional for cloud deployment: Node.js, Serverless Framework, and AWS credentials

## Local Setup

### 1. Verify Python
```bash
python --version
```
On some Linux/macOS systems use `python3`.

### 2. Create virtual environment
```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

Linux/macOS:
```bash
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Initialize database
```bash
python src/database.py
```

### 5. Run application
```bash
python src/app.py
```

### 6. Run tests
```bash
python -m pytest
```

## Serverless / AWS Configuration
`serverless.yml` defines an AWS Lambda-ready health endpoint. The local CLI application does not require AWS credentials, so an evaluator can run and test the project offline.

For deployment, install Node.js and Serverless Framework, configure AWS credentials, then use:
```bash
npm install -g serverless
serverless deploy
```

The cloud deployment section is intentionally separated from local execution so the project remains executable in a clean terminal environment.

## Architecture
User -> CLI/Application -> Business Logic -> Database

Cloud-ready extension:
Client -> API Gateway -> AWS Lambda -> Cloud Database/Object Storage

## Database
Local development uses SQLite with:
- students
- results

The production/serverless version can replace SQLite with DynamoDB or another managed database.

## Project Structure
```text
Serverless-Student-Result-Management-System/
├── src/
│   ├── app.py
│   ├── database.py
│   ├── students.py
│   ├── results.py
│   └── handlers/health.py
├── tests/test_app.py
├── data/results.db
├── config/config.example.json
├── sample/sample_data.json
├── docs/Project_Report.docx
├── requirements.txt
├── serverless.yml
├── README.md
└── .gitignore
```

## Notes
This is an educational project. Do not commit AWS access keys or other secrets to GitHub.
