# Мультитенантный групповой чат с анализом документов
<br>
Backend-приложение для создания каналов с чатом и возможность загрузки документов и их анализа через AI

// VIDEO

## Стек используемых технологий:

- python
- Fastapi w/ sqlalchemy, pydantic
- RAG
- websockets
- postgresql
- pgvector

## Запуск локально 



## Структура проекта 
```
backend/
|-- config.py
|-- data.txt
|-- docs
|   |-- 6
|   |   |-- bitcoin.pdf
|   |   |-- ny_criminal.pdf
|   |   `-- Selenium_python.pdf
|   `-- 7
|       |-- bitcoin.pdf
|       |-- Eht.pdf
|       `-- ny_criminal.pdf
|-- main.py
|-- README.md
`-- src
    |-- auth
    |   |-- dependencies.py
    |   |-- exceptions.py
    |   |-- models.py
    |   |-- registration.py
    |   |-- repository.py
    |   |-- router.py
    |   |-- schemas.py
    |   `-- service.py
    |-- chat
    |   |-- dependencies.py
    |   |-- models.py
    |   |-- repository.py
    |   |-- router.py
    |   |-- schemas.py
    |   |-- service.py
    |   |-- test
    |   |   |-- bm25.py
    |   |   |-- index.html
    |   |   `-- script.js
    |   `-- utils.py
    |-- core
    |   |-- custom_types.py
    |   |-- db.py
    |   |-- dependencies.py
    |   |-- exceptions.py
    |   `-- generic_repository.py
    |-- docs
    |   |-- dependencies.py
    |   |-- models.py
    |   |-- process_file.py
    |   |-- repository.py
    |   |-- router.py
    |   |-- schemas.py
    |   `-- service.py
    |-- rag
    |   |-- calculations.py
    |   |-- data.py
    |   |-- dependencies.py
    |   |-- llm_service.py
    |   |-- rag_service.py
    |   `-- retriever.py
    `-- workspaces
        |-- dependencies.py
        |-- exceptions.py
        |-- models.py
        |-- repository.py
        |-- router.py
        |-- schemas.py
        `-- service.py
```

## План на дальнейшее развитие
- redis для websockets
- pgvector search
- деплой
