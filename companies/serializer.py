from rest_framework import serializers
from .models import Stock


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        # attributes to be return
        fields = ('ticker', 'volume')

#         to return all the attributes use
#          fields='__all__'
