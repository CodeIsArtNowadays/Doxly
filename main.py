from loguru import logger

from src.embedding import VectorStorage
from src.data import TEXT_TO_CHUNK
from src.llm_service import llm_service

from src.eval import eval_text, questions


def main():
    logger.info('MAIN | start')
    
    vectors = VectorStorage(text=TEXT_TO_CHUNK)
    
    logger.info(vectors)
    
    query = 'Who invented transformers?'
    
    chunks = vectors.search(query)
    
    user_prompt = f'Context: {chunks}. \n Question: {query}'
    
    logger.success(llm_service.ask_llm(user_prompt))    
    
    logger.info('MAIN | end')
    
def eval():
    vs = VectorStorage(text=eval_text)
    
    
    hr = 0
    for question in questions:
        correct_index = question[1]
        if correct_index == -1:
            continue
        retrieval = vs.search(question[0])

        if vs.chunks[correct_index] in [v.text for v in retrieval]:
            hr += 1
    print(hr)
        
def bm25_test():
    vectors = VectorStorage(text=eval_text)
    
    print(vectors.bm25_search('When did humans first land on the Moon'))
    
    

if __name__ == '__main__':
    bm25_test()