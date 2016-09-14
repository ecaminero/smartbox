# -*- coding: utf-8 -*-
import json, datetime, time, urllib2
from django.http import JsonResponse
from django.core.cache import cache
import xmltodict
import collections
import pprint
pp = pprint.PrettyPrinter(indent=6)

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

def xml_download(func):
    def wrapper(*args, **kwargs):
        url = "https://s3-sa-east-1.amazonaws.com/cmpsbtv/matchs.xml"
        contents = urllib2.urlopen(url)
        result = func(*args, **kwargs)
        result['partidos'] = contents.read()
        return result
    return wrapper

def xml_parser(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        doc = xmltodict.parse(result['partidos'])
        del result['partidos']
        games = []
        for fecha in doc['fixture']['fecha']:
            for game in fecha['partido']:
              if isinstance(game, collections.OrderedDict) and game['estado']['@id'] == u'2':
                ganador = "Empate" if game['goleslocal'] == game['golesvisitante'] else game['@nomGan']
                fecha = "%s %s" % (game['@fecha'], game['@hora'])
                games.append({
                  "ganador": ganador,
                  "partido": game['@nombreEstadio'],
                  "resultado": "%s - %s" % (game['goleslocal'], game['golesvisitante']),
                  "fecha": datetime.datetime.strptime(fecha, "%Y%m%d %H:%M:%S")
                })
        result['partidos'] = games
        return result
    return wrapper


{

},