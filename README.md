# silk-bot

Telegram-бот заметок и напоминаний: FastAPI API + бот, который работает поверх этого API.

## Требования

- Python 3.11+
- [just](https://github.com/casey/just) (для рецептов ниже) — необязательно, все команды есть и в чистом виде

## Установка зависимостей

```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows
.venv\Scripts\activate
pip install -e ".[dev]"
```

Или одной командой:

```bash
just install
```

## Настройка

Скопируйте шаблон окружения и заполните его:

```bash
cp .env.example .env
```

Пример `.env`:

```
TELEGRAM_BOT_TOKEN=1234567890:AAExampleTokenReplaceMe
API_BASE_URL=http://127.0.0.1:8000
API_TIMEOUT=5.0
LOG_LEVEL=INFO
ENVIRONMENT=local
```

Файл `.env` находится в `.gitignore` и не должен попадать в репозиторий. Реальные секреты в репозиторий не добавляются — в `.env.example` лежат только плейсхолдеры.

## Переменные окружения

| Переменная          | Обязательна | По умолчанию          | Назначение                                   |
|---------------------|-------------|-----------------------|----------------------------------------------|
| `TELEGRAM_BOT_TOKEN` | да          | —                     | Токен Telegram-бота от @BotFather             |
| `API_BASE_URL`      | нет         | `http://127.0.0.1:8000` | Базовый URL FastAPI API, к которому ходит бот |
| `API_TIMEOUT`       | нет         | `5.0`                 | Таймаут HTTP-запросов бота к API, в секундах   |
| `LOG_LEVEL`         | нет         | `INFO`                | Уровень логирования                          |
| `ENVIRONMENT`       | нет         | `local`               | Режим окружения (`local`, `prod` и т.п.)      |

## Запуск API

```bash
uvicorn silk_bot.api.main:app --reload --port 8000
```

Или:

```bash
just run-api
```

API поднимется на http://127.0.0.1:8000, Swagger UI — на http://127.0.0.1:8000/docs.

## Проверка health-check

```bash
curl http://127.0.0.1:8000/health
```

Ожидаемый ответ:

```json
{"status":"ok","version":"0.1.0"}
```

## Запуск бота

После настройки переменных окружения (`TELEGRAM_BOT_TOKEN` обязателен):

```bash
python -m silk_bot.bot.main
```

Или:

```bash
just run-bot
```

Команды бота: `/start`, `/health`, `/note <текст>`, `/remind <текст> <время>`.

## Тесты

```bash
just test
```

Рецепт `test` создаёт `.venv`, ставит зависимости с dev-экстрами и запускает pytest — именно эту команду выполняет CI (`.github/workflows/ci.yml`).

## Вне первой версии

Погода и дополнительные уведомления не входят в первую задачу.
