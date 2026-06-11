import aiofiles

from pypdf import PdfReader
from docx import Document


class ProcessFile:

    def __init__(self):
        self.PARSER = {
            'pdf': self.get_text_from_pdf,
            'txt': self.get_text_from_txt,
            'docx': self.get_text_from_docx
        }

    async def __call__(self, file_path: str):
        pass
        # text = parser 
        # chunk text 
        # save chunk 
        # embedd chunk 
        # save vdb

    async def get_text_from_pdf(file_path: str):
        reader = PdfReader(file_path)
        text = '\n'.join(page.extract_text() for page in reader.pages)
        return text
        
    async def get_text_from_txt(file_path):
        async with aiofiles.open(file_path, 'r') as f:
            return f.read()
            
    async def get_text_from_docx(file_path: str):
        file = Document(file_path)
        full_text = []

        for para in file.paragraphs:
            full_text.append(para.text)

        return '\n'.join(full_text)
