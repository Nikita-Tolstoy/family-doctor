# -*- coding: utf-8 -*-
from aiohttp import web
from apps import setup_static_routes, setup_routes
from log import log
from db_models import init_db

if __name__ == '__main__':
    log("INFO", "Старт приложения")
    init_db()
    web_app = web.Application(client_max_size=1024*1024*1024**2)
    setup_routes(web_app)
    setup_static_routes(web_app)
    web.run_app(web_app)
