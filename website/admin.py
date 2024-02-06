from django.contrib import admin
from django.contrib.sessions.models import Session

# Register your models here.
from .models import Cart, Product, Category


class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()

    list_display = ['session_key', '_session_data', 'expire_date']


admin.site.register(Session, SessionAdmin)

# Models
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Category)
