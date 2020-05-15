"""websocket_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.http import JsonResponse
from websocket_app.redis_cli import RedisCli


def trigger_event_view(request):
    redis_cli = RedisCli.get()
    redis_cli.set('trigger_event', 'event')
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path('trigger_event/', trigger_event_view),
]
