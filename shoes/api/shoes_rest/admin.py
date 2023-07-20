from django.contrib import admin
from .models import Shoe, BinVO

@admin.register(Shoe)
class ShoeAdmin(admin.ModelAdmin):
    list_display = (
        "size",
        "manufacturer",
        "model_name",
        "color",
        "picture",
        "bin",
    )

    @admin.register(BinVO)
    class BinVOAdmin(admin.ModelAdmin):
        list_display = (
            "closet_name",
            "bin_number",
            "bin_size",
        )