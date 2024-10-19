from django.apps import AppConfig
import pymysql

class ProtectappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'protectapp'

    HOST="127.0.0.1"
    port = 3307
    USER="root"
    PASSWORD="root"

    conn=pymysql.connect(host=HOST, port=port, user=USER, password=PASSWORD)
    if conn.open:
        with conn.cursor() as cursor:
            print("protectAPP connected")
    conn.close()