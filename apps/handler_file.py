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

    def upload(self, Data_file):
        filename = str(uuid4().hex)
        file_id = self.new_id(filename)
        t = threading.Thread(target=self.save_storage, args=(file_id, Data_file))
        t.start()
        return self.respons_c(200, 200, "File save", file_id)



    def check(self, request):
        id = request.match_info.get('id')
        b_check = self.check_file_storage(id)
        if b_check:
            return self.respons_c(msg="The file is on disk", cid=id)
        else:
            return self.respons_c(404, 404, "No file on disk", id)

    def download(self, request):
        id = request.match_info.get('id')
        file_name = self.get_file_name(id)
        if file_name:
            res = web.FileResponse(BASE_DIR + FILE_STORAGE + id, chunk_size=SIZE_FILE, status=200,
            headers=MultiDict({'Content-Type': str(mimetypes.guess_type(str(BASE_DIR + FILE_STORAGE + id))), 'Content-Disposition':
                    f'attachment; filename="{file_name}"'}))

            return res
        else:
            return self.respons_c(404, 404, "File not found")

    @staticmethod
    def respons_c(code=200, status=200, msg=None, cid=None):
        json_mass = {
                     "code": code,
                     "msg": msg,
                     "cid": cid
                    }
        return web.json_response(json_mass, content_type='application/json', dumps=json.dumps, status=status)


    @staticmethod
    def new_id(name_file):
        log("INFO", "Новая запись БД")
        return str(File.create(id=uuid4(), f_name=name_file).id)

    @staticmethod
    def get_file_name(uuid):
        DS = File.select().where(File.id == uuid)
        if DS:
            return DS[0].f_name
        else:
            return None

    @staticmethod
    def check_file_storage(name_file):
        import os
        return True if os.path.exists(BASE_DIR + FILE_STORAGE + name_file) else False

    @staticmethod
    def save_storage(path, file):
        log("INFO", f"Файл {path} сохранен на диске ")
        with open(BASE_DIR + FILE_STORAGE + path, "wb") as f_handler:
            while True:
                f_handler.write(file)