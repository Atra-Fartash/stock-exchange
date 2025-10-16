from rest_framework.serializers import ModelSerializer
from stock.models import Company, SaleRequest, BuyRequest


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class SaleRequestSerializer(ModelSerializer):
    class Meta:
        model = SaleRequest
        fields = '__all__'


class BuyRequestSerializer(ModelSerializer):
    class Meta:
        model = BuyRequest
        fields = '__all__'