import os
import secrets
import requests

from testapi.settings import TELEGRAM_BOT_TOKEN
from users.models import User
from loguru import logger

logger.add('test_api_debug.log', format="{time} {level} {message}",
           level="DEBUG", rotation="10:00", compression=zip
           )


def generate_token_for_telegram():
    """Генерирует токен для телеграмм"""
    token = secrets.token_hex(16)
    return token


def add_chat_id_in_user(user, chat_id):
    """Добавляет пользоватулю chat_id телеграмма"""
    user.chat_id = chat_id
    user.save()
    return "Пользователь добавлен"


def find_telegram_token(token, chat_id):
    """Получает пользователя по токену"""
    try:
        user = User.objects.get(telegram_token=token)
        if user:
            add_token_result = add_chat_id_in_user(user, chat_id)
            return add_token_result
    except User.DoesNotExist:
        return "Can't find token"


def check_telegram_token(token, chat_id):
    """Проверяет полученный токен"""
    result = find_telegram_token(token, chat_id)
    return result

@logger.catch
def send_message_to_telegram(chat_id, user, text):
    logger.debug(f'send_message_to_telegram params {chat_id}, {user}, {text}')
    """Отправляет сообщение в телеграмм"""
    message = f'{user}, я получил от тебя сообщение:\n{text}'
    data = {'chat_id': chat_id, 'text': message}
    requests.post(f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage', json=data)
