python_bin := if os() == "windows" { "python" } else { "python3" }
venv_py    := if os() == "windows" { ".venv/Scripts/python.exe" } else { ".venv/bin/python" }

# Создать venv и установить зависимости
install:
    {{python_bin}} -m venv .venv
    {{venv_py}} -m pip install --upgrade pip
    {{venv_py}} -m pip install -e ".[dev]"

# Запустить API локально (http://127.0.0.1:8000/health)
run-api:
    {{venv_py}} -m uvicorn silk_bot.api.main:app --reload --port 8000

# Запустить бота (нужны переменные окружения)
run-bot:
    {{venv_py}} -m silk_bot.bot.main

# То, что запускает CI
test:
    {{python_bin}} -m venv .venv
    {{venv_py}} -m pip install --upgrade pip
    {{venv_py}} -m pip install -e ".[dev]"
    {{venv_py}} -m pytest
