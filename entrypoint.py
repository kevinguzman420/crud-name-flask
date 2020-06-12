# entrypoint 

import os

from app import create_app

settings_module = os.getenv('APP_SETTINGS_MODULE') # export APP_SETTINGS_MODULE="config.entorno_nombre"
app = create_app(settings_module)