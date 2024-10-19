from django.apps import AppConfig
import pymysql


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    HOST="127.0.0.1"
    PORT=3307
    USER="root"
    PASSWORD="root"

    conn=pymysql.connect(host=HOST, port=PORT, user=USER, password=PASSWORD)
    if conn.open:
        with conn.cursor() as cursor:
            print("connected")
    conn.close()