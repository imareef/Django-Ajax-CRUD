from django.contrib import admin

from crud_ajax.models import CrudUser


@admin.register(CrudUser)
class CrudUserAdmin(admin.ModelAdmin):
    pass

