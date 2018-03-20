from django.contrib import admin
from explorescotland.models import ParentProfile, Feedback, ChildProfile, Level, QuizQuestion

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('message', 'date', 'parent')

class ParentAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'birthdate')

class ChildAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'parent')

class LevelAdmin(admin.ModelAdmin):
    list_display =('number', 'topic', 'content')

class QuizAdmin(admin.ModelAdmin):
    list_display = ('question_id', 'question', 'correctAnswer',
                    'incorrectAnswer1', 'incorrectAnswer2',
                    'incorrectAnswer3', 'level')

admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(ParentProfile, ParentAdmin)
admin.site.register(ChildProfile, ChildAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(QuizQuestion, QuizAdmin)
