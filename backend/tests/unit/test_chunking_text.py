import pytest


@pytest.mark.asyncio(loop_scope="class")
class TestChunking:

    @pytest.fixture(scope='class', autouse=True)
    @classmethod
    def setup_service(self, request):
        from src.docs.process_file import ProcessFile
        service = ProcessFile(chunk_repo=None, document_repo=None)
        request.cls.service = service
    
    async def test_max_length(self):
        text = 'word' * 1000
        chunks = await self.service.chunking_text(text, size=300, overlap=20)
        assert all(len(c) <= 300 for c in chunks)

    async def test_overlap_between_chunks(self):
        text = 'abcdefghijklmo' * 1000
        chunks = await self.service.chunking_text(text, size=300, overlap=20)
        assert chunks[0]['text'][-20:] == chunks[1]['text'][:20]

    async def test_short_text(self):
        chunks = await self.service.chunking_text('simple text', size=300, overlap=20)
        assert len(chunks) == 1