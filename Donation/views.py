from django.shortcuts import render
from django.http import JsonResponse
from backend.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
# create your views here 
# def  apioverview(request):
#     return JsonResponse("this is for test",safe=False)
@api_view(['GET'])
# create your views here 
def apioverview(request):
    api_urls={
    'this is get data in api',
    'this is get and post method in api'
    }
    return Response(api_urls)

