# AI-Powered Resume Analyzer

## How to run this app:

Clone this repository:

    git clone https://github.com/UIika/AI-Powered-Resume-Analyzer
    cd AI-Powered-Resume-Analyzer

Create ".env" file and add environment variables to it:
```dotenv
APP_SECRET_KEY="<your_app_secret_key>"
GEMINI_API_KEY="<your_gemini_api_key>"
```

Install poetry:

    pip install poetry

Create virtual environment and install project dependencies:

    poetry install

Activate virtual environment:

    eval $(poetry env activate)  # in Bash(Linux)
    Invoke-Expression (poetry env activate)  # in Powershell(Windows)

Run app:

    uvicorn src.main:app --reload
