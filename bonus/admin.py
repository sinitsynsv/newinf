from django.contrib import admin

from .models import AccountPayment, AccountPaymentService, User, BonusTransaction


admin.site.register(AccountPayment)
admin.site.register(AccountPaymentService)
admin.site.register(User)
admin.site.register(BonusTransaction)
