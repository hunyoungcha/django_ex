from django.shortcuts import render
from django.db import connection

# Create your views here.

def index(request):
    input = request.GET.get('input', '')
    query = "select * from protectapp_protectpy5test where name = %s "

    with (connection.cursor() as cursor):
        cursor.execute(query, [input])
        rows=cursor.fetchall()

        context = {
            'rows':rows,
        }

        return
        render(request, 'protectapp/index.html', context)