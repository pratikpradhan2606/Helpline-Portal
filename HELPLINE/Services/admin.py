from django.contrib import admin
from .models import Numbers, Emergency, Manchar
# Register your models here.
admin.site.register(Numbers),
admin.site.register(Emergency),
admin.site.register(Manchar)
