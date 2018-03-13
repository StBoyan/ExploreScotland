from django.contrib import admin
from explorescotland.models import ParentProfile, Feedback, ChildProfile

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('message', 'date', 'parent')

class ParentAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'birthdate')

class ChildAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'parent')

admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(ParentProfile, ParentAdmin)
admin.site.register(ChildProfile, ChildAdmin)
