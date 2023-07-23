from django.contrib import admin
from .models import BinVO

@admin.register(BinVO)
class BinVOAdmin(admin.ModelAdmin):
    pass
