from rest_framework import serializers
from .models import BonusTransaction

class BonusTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BonusTransaction
        fields = ['id', 'user', 'account_payment', 'value', 'note'] #'date_created', 'date_updated']