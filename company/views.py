from django.shortcuts import render
from django.http import HttpResponse
from config import config

import sys
sys.path.append('..')


def index(request):
    db = config.DatabaseConfig()
    return HttpResponse(db.name+ " "+db.user)
