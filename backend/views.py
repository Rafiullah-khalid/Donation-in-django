from rest_framework.generics import ListCreateAPIView
from .models import Category, Product
from .Serlizers import ProductSerializer,CategorySerializer
# Create your views here.

class ProductViewSet(ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer


class CategoryViewSet(ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer