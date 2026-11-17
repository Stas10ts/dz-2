# Практическая работа: Pydantic v2 + Context7 MCP

## Запуск
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
pip install -r requirements.txt
pytest
```

## Задание
1. В VS Code подключите Context7 MCP и убедитесь, что инструменты
   `resolve-library-id` и `get-library-docs` доступны в Agent.
2. Откройте `src/order_processor.py`.
3. В Copilot Chat выберите Agent и запустите `/pydantic-upgrade`.
4. Подтверждайте запросы агента на чтение документации Context7.
5. Проверьте изменения в Source Control.
6. Запустите `ruff check --fix .` и `pytest`.

Исходный модуль намеренно использует конструкции Pydantic v1:
`@validator`, `class Config`, `orm_mode`, `.dict()`.
Агент должен перевести их на Pydantic v2.
