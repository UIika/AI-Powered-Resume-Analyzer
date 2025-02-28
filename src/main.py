import os

from fastapi import FastAPI, UploadFile, HTTPException, Request, File, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from dotenv import load_dotenv
import markdown

from src.parser import parse_resume_file
from src.ai import analyze_resume


load_dotenv()

app = FastAPI(title='AI-Powered Resume Analyzer')
app.add_middleware(SessionMiddleware, secret_key=os.getenv('APP_SECRET_KEY'))

templates = Jinja2Templates(directory='src/templates')
app.mount('/static', StaticFiles(directory='src/static'), name='static')


@app.post('/api/')
async def api(
    resume_file: UploadFile = File(...),
    job_description: str = Form(...),
):
    try:
        resume_text = await parse_resume_file(resume_file)
    except KeyError:
        raise HTTPException(status_code=400, detail='File type is not supported')

    feedback = analyze_resume(resume_text, job_description)

    return {'feedback': feedback}


@app.get('/')
async def homepage(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.post('/')
async def homepage(  # noqa: F811
    request: Request,
    resume_file: UploadFile = File(...),
    job_description: str = Form(...)
):
    try:
        resume_text = await parse_resume_file(resume_file)
    except KeyError:
        request.session['flash'] = 'File type is not supported'
        return RedirectResponse('/', status_code=303)

    feedback = analyze_resume(resume_text, job_description)

    return templates.TemplateResponse('index.html', {
        'request': request, 'feedback': markdown.markdown(feedback)
    })
