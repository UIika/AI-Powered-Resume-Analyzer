import io
import docx
import PyPDF2
from abc import ABC, abstractmethod

from fastapi import UploadFile


class ResumeParser(ABC):
    @abstractmethod
    def extract_text(self, file: bytes) -> str:
        pass


class DocxParser(ResumeParser):
    def extract_text(self, file: bytes) -> str:
        doc = docx.Document(io.BytesIO(file))
        return '\n'.join([paragraph.text for paragraph in doc.paragraphs])


class PdfParser(ResumeParser):
    def extract_text(self, file: bytes) -> str:
        reader = PyPDF2.PdfReader(io.BytesIO(file))
        return '\n'.join([page.extract_text() for page in reader.pages if page.extract_text()])


available_parsers = {
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document': DocxParser(),
    'application/pdf': PdfParser()
}


async def parse_resume_file(resume_file: UploadFile) -> str:
    '''Returns resume file text or raises KeyError if file type is not supported'''
    parser: ResumeParser = available_parsers[resume_file.content_type]
    return parser.extract_text(await resume_file.read())
