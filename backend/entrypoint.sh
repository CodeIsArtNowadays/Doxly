#!/bin/sh
set -e

echo "Применяем миграции Alembic..."
uv run alembic upgrade head

echo "Запускаем приложение..."
exec "$@"
