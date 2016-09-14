# -*- coding: utf-8 -*-
import json, datetime
from django.shortcuts import render
from django.http import JsonResponse


def json_converter(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return JsonResponse(result)
    return wrapper

def datetime_decorator(func):
    def wrapper(*args, **kwargs):
        now = datetime.datetime.now()
        result = func(*args, **kwargs)
        result['datetime'] = now.isoformat()
        return result
    return wrapper


# Create your views here.
@json_converter
@datetime_decorator
def index(request):
    completed_in = 0;
    response = {
      "completed_in": completed_in,
      "c": { "d": "e" },
      "a": "b" 
    }
    return response

