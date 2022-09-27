from django.contrib import admin
from . import models
from django.db.models import Count
# Register your models here.


@admin.register(models.Bio)
class BioAdmin(admin.ModelAdmin):
    list_display = ['name', 'title']
    list_editable = ['title']
    list_per_page = 10
    list_filter = ['name', 'updated']
    search_fields = ['title__istartswith']


@admin.register(models.Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['skill_name']
    list_per_page = 10


@admin.register(models.Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'link']


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'technology', 'image']
