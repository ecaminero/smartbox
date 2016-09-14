# -*- coding: utf-8 -*-
import json, datetime, time
from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache


# Decorators
def json_converter(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return JsonResponse(result)
    return wrapper

def datetime_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        now = datetime.datetime.now()
        result['datetime'] = now.isoformat()
        return result
    return wrapper

def execution_time(func):
    def wrapper(*args):
        time1, result, time2 = time.time(), func(*args), time.time()
        result['completed_in'] = round((time2-time1)*1000.0, 4)
        return result
    return wrapper

def cache_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not cache.get('data'):
          cache.set('data', result, 5)
          time.sleep(2)
        return result
    return wrapper
# Create your views here.

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

