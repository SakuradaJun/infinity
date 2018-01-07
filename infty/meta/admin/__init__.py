from django.contrib import admin

from infty.meta.models import Type, Schema, Instance
from infty.meta.admin.forms import TypeForm, SchemaForm, InstanceForm


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    form = TypeForm

@admin.register(Schema)
class SchemaAdmin(admin.ModelAdmin):
    form = SchemaForm

@admin.register(Instance)
class InstanceModelAdmin(admin.ModelAdmin):
    form = InstanceForm
