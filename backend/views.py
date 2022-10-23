from itertools import product
from rest_framework.generics import ListCreateAPIView
from .models import Category, Product
from .Serlizers import ProductSerializer,CategorySerializer
from rest_framework import generics

# Create your views here.

class ProductViewSet(ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer


class CategoryViewSet(ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class ProductUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product
    serializer_class=ProductSerializer






















# from rest_framework.decorators import api_view
# from rest_framework.response import Response


# @api_view(['GET'])
# # create your views here 
# def apioverview(request):
#     api_urls={
#     'this is get data in api',
#     'this is get and post method in api'
#     }
#     return Response(api_urls)

# @api_view(['GET'])
# def Proview(request):
#     product=Product.objects.all()
#     serlizer=ProductSerializer(product,many=True)
#     return Response(serlizer.data)


# @api_view(['GET'])
# def Prosearch(request,pk):
#     product=Product.objects.get(id=pk)
#     serlizer=ProductSerializer(product,many=False)
#     return Response(serlizer.data)   



# @api_view(['POST'])
# def Procreate(request):
#     # product=Product.objects.get(id=pk)
#     serlizer=ProductSerializer(data=request.data)

#     if serlizer.is_valid():
#         serlizer.save()

#     return Response(serlizer.data)   



# @api_view(['POST'])
# def Proupdate(request,pk):
#     produc=Product.objects.get(id=pk)
#     serlizer=ProductSerializer(instance=produc,data=request.data)

#     if serlizer.is_valid():
#         serlizer.save()

#     return Response(serlizer.data)   








