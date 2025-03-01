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

## How to use this app:

Open your browser and go to:

    http://localhost:8000/

Here, you can upload your resume and enter a job description.

![image](https://github.com/user-attachments/assets/cfd36de4-9482-4ca3-ad83-955d9b96a336)

## API usage:

Endpoint: POST /api/

Content-Type: multipart/form-data

Parameters:

    resume_file (file): The resume file to be analyzed (docx/pdf).
    job_description (string): The job description text.
    
Example Request (cURL)

    curl -X POST "http://localhost:8000/api/" \
         -F "resume_file=@path/to/resume.pdf" \
         -F "job_description=Looking for a Python developer with 3+ years of experience."
         
Example Response

    {
      "feedback": "Your resume is a good match. Consider adding more details about Python projects."
    }
    
Now you're ready to analyze resumes efficiently! 🚀
