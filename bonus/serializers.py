from rest_framework import serializers
from .models import BonusTransaction

# class BonusTransactionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BonusTransaction
#         fields = ['id', 'user', 'account_payment', 'value', 'note'] #'date_created', 'date_updated']

class BonusTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BonusTransaction
        fields = ['id', 'user', 'value', 'note']# 'date_created', 'date_updated']
    # для Serializer 
    # id = serializers.IntegerField(read_only=True)
    # user = serializers.StringRelatedField(many=False)
    # value = serializers.DecimalField(max_digits=20, decimal_places=2)
    # note = serializers.CharField(max_length=200)
    # date_created = serializers.DateTimeField()
    # date_updated = serializers.DateTimeField()