import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
#from django.core.asgi import get_asgi_application
import chart.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "livechart.settings")

application = ProtocolTypeRouter({
  "websocket": AuthMiddlewareStack(
        URLRouter(
            chart.routing.websocket_urlpatterns
        )
    ),
})
