from django.db import connection

def fetch_data():
    with connection.cursor() as cursor:
        cursor.execute("select * from books")

        rows = cursor.fetchall()

        for row in rows:
            print(row)