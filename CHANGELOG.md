# CHANGELOG — telegram-bot-1 (BreadFastBot, проверочная М1)

## Что сделано
- `main.py` — регистрация экземпляра `Bot` и отправка первого сообщения себе.
  Секреты (токен, chat_id) читаются из `.env` через `python-dotenv` —
  репозиторий уходит в Git, поэтому хардкода нет.
- Реализовано строго под контракт автотестов (`test.py`):
  - `from telegram import Bot` (тест: `main.Bot`);
  - экземпляр назван `bot` (тест: `isinstance(main.bot, telegram.Bot)`);
  - переменные `chat_id`, `text` (обе строки);
  - вызов `bot.send_message(chat_id, text)` — **позиционно** (тест:
    `assert_called_once_with(chat_id, text)`).
- `.gitignore` — `.env`, `*.session`, `.venv`, кэши (добавлен: в шаблоне его нет).

## Версия библиотеки
- `python-telegram-bot==13.7` (синхронная) — как требует README и тесты.
  Тренажёрная проверочная под фиксированную версию; async-стандарт проекта
  (v21/v22) здесь намеренно не применяется.
- Под v13.7 нужен Python **3.10** (на 3.12 старая библиотека не встаёт).

## Окружение (uv, наш стек вместо venv/pip из README)
```bash
cd telegram-bot-1
uv venv --python 3.10
uv pip install python-telegram-bot==13.7 python-dotenv
```

## .env (в корень репо, рядом с main.py)
```
BOT_TOKEN=<токен от @BotFather: /token>
MY_CHAT_ID=725856695
```
- Без `.env` (или пустого BOT_TOKEN) импорт main упадёт с `KeyError`.
- `.env` в `.gitignore` — в Git не уходит.

## Проверка (из корня репо)
```bash
uv run python test.py     # автотесты → "Все тесты прошли успешно."
uv run python main.py     # реальная отправка — придёт сообщение в Telegram
```
Перед `main.py` нажать в чате с ботом кнопку **Start** (бот не пишет первым).

## После сдачи
- Отозвать токен: @BotFather → /revoke (токен светился ранее).

## Git (ветка форка — main)
```bash
git add main.py CHANGELOG.md .gitignore
git status                 # убедиться: .env и .venv НЕ в индексе
git commit -m "BreadFastBot: отправка первого сообщения (проверочная М1)"
git push origin main
```
