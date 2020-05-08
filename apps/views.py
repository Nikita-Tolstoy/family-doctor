# -*- coding: utf-8 -*-
import aiohttp_jinja2
from .handler_index import DataSet
from .handler_file import H_File

@aiohttp_jinja2.template('index.html')
async def h_index(request):
    return DataSet(request)

async def h_Upload(request):
    data_file = await request.read()
    return H_File().upload(data_file)

async def h_Check(request):
    return H_File().check(request)

async def h_Download(request):
    return H_File().download(request)

