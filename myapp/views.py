from django.shortcuts import render
from django.db import connection


def index(request):
    with connection.cursor() as cursor:
        input = request.GET.get('input')
        query = f"select * from myapp_py5test where name = '{input}' "
        cursor.execute(query)

        rows= cursor.fetchall()

        context = {
            'rows':rows,

        }

        return render(request, 'myapp/index.html', context)


