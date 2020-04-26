# -*- coding: utf-8 -*-
from aiohttp import web
import aiohttp_jinja2
import jinja2

from setting import BASE_DIR, SIZE_FILE
from apps.views import h_index, h_Upload, h_Check, h_Download

def setup_routes(web_app):
    web_app.add_routes([
    web.get('/', h_index),
    web.post('/upload', h_Upload),
    web.get('/check/{id}', h_Check),
    web.get('/download/{id}', h_Download),
    ])


def setup_static_routes(web_app):
    web_app.router.add_static('/static/',
                          path=BASE_DIR + '/apps/static/',
                          name='static',
                          chunk_size=SIZE_FILE)
    aiohttp_jinja2.setup(web_app,
                         loader=jinja2.FileSystemLoader(BASE_DIR + '/apps/templates/'))