# -*- coding: utf-8 -*-
from .decorators import json_converter, datetime_decorator
from .decorators import execution_time, cache_decorator
from .decorators import xml_download, xml_parser

@json_converter
@cache_decorator
@execution_time
@datetime_decorator
def index(request):
    response = {
      "c": { "d": "e" },
      "a": "b" 
    }
    return response

@json_converter
@execution_time
@datetime_decorator
@xml_parser
@xml_download
def futbol(request):
    response = {
    }
    return response
