import os
from google import genai
from google.genai import types
from dotenv import load_dotenv


load_dotenv()


ai_client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))


def analyze_resume(resume_text: str, job_description: str) -> str:

    prompt = f'''
    Compare the following resume with the job description and provide feedback.

    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Provide feedback highlighting missing skills, improvement suggestions, and a summary.
    '''

    response = ai_client.models.generate_content(
        model='gemini-2.0-flash',
        config=types.GenerateContentConfig(system_instruction='You are an expert HR analyst.'),
        contents=[prompt]
    )
    return response.text
