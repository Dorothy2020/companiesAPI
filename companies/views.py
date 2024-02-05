from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Stock
from .serializer import StockSerializer


# Create your views here.

# list all stocks or create a new one
# stocks/

class StockList(APIView):

    #  get method will return all stock information
    def get(self, request):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)

    def post(self):
        pass
