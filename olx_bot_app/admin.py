from django.contrib import admin
from olx_bot_app.models import Ad, Subscriber

# admin.site.register(Ad)
# admin.site.register(City)
admin.site.register(Subscriber)


@admin.register(Ad)
class AdsAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'url', 'city', 'metrs')





