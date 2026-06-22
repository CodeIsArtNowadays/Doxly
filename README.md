# Мультитенантный групповой чат с анализом документов
<br>
Backend-приложение для создания каналов с чатом и возможность загрузки документов и их анализа через AI

// VIDEO

## MVP
- Регистрация/Авторизация
- Создание воркспейсов
- Добавление участников в воркспейс хозяевами (owner)
- Ограничение доступа по принадлежности к воркспейсу, и правам
- Внутриканальный чат
- Загрузка в воркспейс документов
- Вопрос к ллм по документам в чате через "@ai"

## Стек используемых технологий:
- python
- Fastapi w/ sqlalchemy, pydantic
- openai, openrouter, sentence-transformers
- websockets
- postgresql
- pgvector

## Запуск локально 

## Архитектура
Основная backend логика реализованна по типу роут - сервис - репозиторий. Уровень роута принимает данные по http протоколам, обрабатывает вебсокет и проверяет наличие прав доступа (member, admin, owner) через DI. Уровень репозитория взаимоодействует с бд. Сервис связывает роуты и репозитории.
Проект разбит на логические части - приложения: auth, workspaces, chat, docs, rag. Приложение core - системное, используется в каждом из других.
Для авторизации в приложении auth используется JWT токен. Процесс регистрации вынесен в use case registration.py из-за создания сторонней модели Member. 
Приложения workspaces, chat, docs - обрабатывают создание каналов, соединение с чатом, загрузку и обработку документов.
Приложение rag реализует выборку чанков, нахождение схожести по гибридному (cosine similarity + bm25) поиску, и запрос к ллм.

## Структура проекта 
```backend/
|-- config.py
|-- data.txt
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
- тесты
- расширение функционала разных прав доступа
