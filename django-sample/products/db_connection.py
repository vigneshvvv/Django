from django.db import connection

def get_product_details():
    with connection.cursor() as cursor:
        cursor.execute("select * from Products")
        rows = cursor.fetchall()
    return rows