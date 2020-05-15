"""
ASGI config for websockets project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from websocket_app.websocket_application import websocket_application
from websocket_app.redis_cli import RedisCli

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websocket_app.settings')

django_application = get_asgi_application()


async def application(scope, receive, send):
    RedisCli.get()
    if scope['type'] == 'http':
        await django_application(scope, receive, send)
    elif scope['type'] == 'websocket':
        await websocket_application(scope, receive, send)
    else:
        raise NotImplementedError(f"Unknown scope type {scope['type']}")
