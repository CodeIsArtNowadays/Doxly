from loguru import logger

from src.config import AI_KEY
from src.embedding import VectorStorage, Vector
from src.data import TEXT_TO_CHUNK
from src.llm_service import llm_service


def main():
    logger.info(f'MAIN | start')
    
    vectors_texts = ['king', 'dog', 'England', 'pink', 'rap']
    vectors = VectorStorage(text=TEXT_TO_CHUNK)
    for i in vectors_texts:
        vectors.add_vector(Vector(i))
    
    logger.info(vectors)
    
    query = 'Who invented transformers?'
    
    chunks = vectors.search(query)
    
    user_prompt = f'Context: {chunks}. \n Question: {query}'
    
    logger.success(llm_service.ask_llm(user_prompt))    
    
    logger.info('MAIN | end')
    
if __name__ == '__main__':
    main()