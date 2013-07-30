from django.contrib import admin
from financial.models import User
from financial.models import Golden
from financial.models import Transaction
from financial.models import Balance

admin.site.register(User)
admin.site.register(Golden)
admin.site.register(Transaction)
admin.site.register(Balance)