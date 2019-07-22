from django.contrib import admin
from . models import myusers

class userdata(admin.ModelAdmin):
    fields = [
        "stock",
        "uid"
    ]

admin.site.register(myusers, userdata)

