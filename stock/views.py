from stock.models import Company, SaleRequest, BuyRequest
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from stock.serializers import CompanySerializer, SaleRequestSerializer, BuyRequestSerializer


class SaleRequestListCreate(ListCreateAPIView):
    queryset = SaleRequest.objects.all()
    serializer_class = SaleRequestSerializer


class SaleRequestDestroyUpdateRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = SaleRequest.objects.all()
    serializer_class = SaleRequestSerializer