from django.urls import path
from stock.views import SaleRequestListCreate, SaleRequestDestroyUpdateRetrieve


urlpatterns = [
    path('sale-request-list-create', SaleRequestListCreate.as_view()),
    path('sale-request-retrieve-destroy-update/<str:pk>', SaleRequestDestroyUpdateRetrieve.as_view()),
]