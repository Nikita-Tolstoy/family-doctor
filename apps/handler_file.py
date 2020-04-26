# -*- coding: utf-8 -*-
from aiohttp import web
import mimetypes
from db_models import File
from setting import BASE_DIR, FILE_STORAGE, SIZE_FILE
from log import log
from uuid import uuid4
import json
import threading
from multidict import MultiDict

class H_File:
    def __init__(self):
        pass

    def Upload(self, Data_file):
        file = Data_file['files'].file
        filename = Data_file['files'].filename
        file_id = self.new_id(filename)
        t = threading.Thread(target=self.save_storage, args=(file_id, file))
        t.start()
        self.save_storage(file_id, file)

        raise web.HTTPFound(location='/')

    def save_storage(self, path, file):
        log("INFO", f"Файл {path} получен ")
        with open(BASE_DIR + FILE_STORAGE + path, "wb") as f_handler:
            while True:
                chunk = file.read()
                if not chunk:
                    break
                f_handler.write(chunk)
        log("INFO", f"Файл {path} сохранен на диске")

    def Check(self, request):

        id = request.match_info.get('id')
        b_check = self.check_file_storage(id)
        json_mass = {"id": id,
               "check file": b_check,
               "msg": "The file is on disk" if b_check else "No file on disk"}
        return web.json_response(json_mass, content_type='application/json', dumps=json.dumps)


    def Download(self, request):
        id = request.match_info.get('id')
        file_name = self.get_file_name(id)
        res = web.FileResponse(BASE_DIR + FILE_STORAGE + id,chunk_size=SIZE_FILE, status=200,
            headers=MultiDict({'Content-Type': str(mimetypes.guess_type(str(BASE_DIR + FILE_STORAGE + id))), 'Content-Disposition':
                    f'attachment; filename="{file_name}"'}))

        return res


    def new_id(self, name_file):
        log("INFO", "Новая запись БД")
        return str(File.create(id=uuid4(), f_name=name_file).id)


    def get_file_name(self, uuid):
        return File.select().where(File.id == uuid)[0].f_name


    def check_file_storage(self, name_file):
        import os
        return True if os.path.exists(BASE_DIR + FILE_STORAGE + name_file) else False
