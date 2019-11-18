from . import views
from django.urls import path

urlpatterns = [
    path('', views.testrequest),
    path('GetAllTransactions/', views.ReturnAllUserTransactions),
    path('GetTransactionsSum/', views.ReturnUserTransactionSum),
]