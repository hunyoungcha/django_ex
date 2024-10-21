from django.shortcuts import render
from django.db import connection


def index(request):
    context={}

    if request.method == 'POST':
        input = request.POST.get('input')
        query = f"select * from myapp_py5test where name = '{input}' "

        with connection.cursor() as cursor:
            cursor.execute(query)

            rows= cursor.fetchall()

            context = {
                'rows':rows,

            }

    return render(request, 'myapp/index.html', context)

