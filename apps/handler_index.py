# -*- coding: utf-8 -*-
from db_models import File

def DataSet(req):
    DS = {"files": File.select()}
    return DS