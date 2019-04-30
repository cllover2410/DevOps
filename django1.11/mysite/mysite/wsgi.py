"""
WSGI config for mysite project.
用于mysite项目的wsgi配置。

It exposes the WSGI callable as a module-level variable named ``application``.
它将wsgi可调用公开为一个名为``application``的模块级变量。

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = get_wsgi_application()
