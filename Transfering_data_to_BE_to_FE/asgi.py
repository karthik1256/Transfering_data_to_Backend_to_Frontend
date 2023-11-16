"""
ASGI config for Transfering_data_to_BE_to_FE project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Transfering_data_to_BE_to_FE.settings')

application = get_asgi_application()
