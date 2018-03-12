from django.contrib import admin
from explorescotland.models import ParentProfile, Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('message', 'date', 'parent')

class ParentAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'birthdate')

admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(ParentProfile, ParentAdmin)
