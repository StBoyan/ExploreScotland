from django.db import models
from django.contrib.auth.models import User     # Need to include __str__ functions (same as toString)
from django.utils import timezone
# Reduce max length of most attributes...
class ParentProfile(models.Model):         # This model may actually be unnecessary if there is
    user = models.OneToOneField(User)   # nothing else stored in here (e.g. profile pic)

class Feedback(models.Model):
    message = models.CharField(max_length=2000)
    date = models.DateTimeField(default=timezone.now()) # may need to import something here
    parent = models.ForeignKey(ParentProfile)

class ChildProfile(models.Model):           # Will probably need some attributes or more likely another model
    parent = models.ForeignKey(ParentProfile)  # to store the kids results for display in statistics (for parents)
    name = models.CharField(max_length=128)
    level = models.IntegerField(default=1)  # Assume kids start level 1. This field is probably wrong.. need to look into  how to access level

class Level(models.Model):  # Need to find out how to access model ID
    name = models.CharField(max_length=128, unique=True) # E.g. "Level 1"
# Level and MaterialSubject may be optimised... need to consider this
class MaterialSubject(models.Model):
    name = models.CharField(max_length=128, unique=True) # E.g. "Lochs of Scotland"
    level = models.ForeignKey(Level)

class Material(models.Model):
    name = models.CharField(max_length=128, unique=True) # E.g. "Loch Lomond" [attribute not in original ER]
    content = models.CharField(max_length=2000) # E.g. "Loch Lomond is the biggest loch in Scotland..."
    subject = models.ForeignKey(MaterialSubject)

class QuizQuestion(models.Model):   # some sort of Questionid may be needed here
    difficulty = models.IntegerField(default=0) #may need to drop this one
    question = models.CharField(max_length=128, unique=True) # E.g. "What is the biggest loch in Scotland?"
    CorrectAnswer = models.CharField(max_length=128) # E.g. "Loch Lomond"
    incorrectAnswer1 = models.CharField(max_length=128) # E.g "Loch Ness"
    incorrectAnswer2 = models.CharField(max_length=128) # E.g. "Loch Awe"
    incorrectAnswer3 = models.CharField(max_length=128) # E.g. "Loch Katrine"
    subject = models.ForeignKey(MaterialSubject)
