import aiofiles

from pathlib import Path

from src.docs.repository import DocumentRepository


class DocumentService:

    def __init__(self, repo: DocumentRepository):
        self.repo = repo

    async def save_file(self, workspace_id: int, file):
        upload_dir = Path(f'docs/{workspace_id}')
        upload_dir.mkdir(parents=True, exist_ok=True)
        file_path = upload_dir / file.filename

        async with aiofiles.open(file_path, 'wb') as f:
            while content := await file.read(1024 * 1024):
                await f.write(content)

        return str(file_path)

    