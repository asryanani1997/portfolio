from django.contrib import admin
from .models import Skill, Experience, Education, Message, PortfolioProject


class EducationAdmin(admin.ModelAdmin):
    list_display = ["university_name", "start_date", "end_date", "degree", "created_on"]
    list_filter =["start_date"]

class SkillAdmin(admin.ModelAdmin):
    list_display = ["name", "value"]
    list_filter =["value"]
    search_fields=["name"]

# Register your models here.
admin.site.register(Skill, SkillAdmin)
admin.site.register(Experience)
admin.site.register(Education, EducationAdmin)
admin.site.register(Message)
admin.site.register(PortfolioProject)
