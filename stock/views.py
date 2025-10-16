from stock.models import Company, SaleRequest, BuyRequest
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from stock.serializers import CompanySerializer, SaleRequestSerializer, BuyRequestSerializer



def check_request():
    sale_request_sort = SaleRequest.objects.all().order_by('-price')
    buy_request_sort = BuyRequest.objects.all().order_by('price')
    for i in sale_request_sort:
        for j in buy_request_sort:
            if i <= j:
                BuyRequest.amount - SaleRequest.amount


class SaleRequestListCreate(ListCreateAPIView):
    queryset = SaleRequest.objects.all()
    serializer_class = SaleRequestSerializer


class SaleRequestDestroyUpdateRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = SaleRequest.objects.all()
    serializer_class = SaleRequestSerializer


class BuyRequestCreate(CreateAPIView):
    queryset = BuyRequest.objects.all()
    serializer_class = BuyRequestSerializer

