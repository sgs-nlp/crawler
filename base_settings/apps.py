"""
base_settings.apps.py
"""
from django.apps import AppConfig


class BaseSettingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_settings'
