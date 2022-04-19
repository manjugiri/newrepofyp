from django.contrib import admin
from .models import  ApplyAgent, Properti, Bank,AgentRating

admin.site.register(Properti)
admin.site.register(Bank)
admin.site.register([ApplyAgent,AgentRating])
