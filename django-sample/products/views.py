from django.shortcuts import render
from django.http import JsonResponse
from . import db_connection

def getProductInfo():
    data = db_connection.get_product_details()
    if data is None:
        return JsonResponse({"Error": "Product Data Not Found"})
    return JsonResponse(data)
