from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
# Reduce max length of most attributes...
class ParentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # TODO include gender, birthdate
                                                            
    def __str__(self):
        return self.user.username

class Feedback(models.Model):
    message = models.CharField(max_length=2000)
    date = models.DateTimeField(default=timezone.now()) # may need to import something here
    parent = models.ForeignKey(User)

class ChildProfile(models.Model):           # TODO Will probably need some attributes or more likely another model
    parent = models.ForeignKey(User)  # to store the kids results for display in statistics (for parents)
    name = models.CharField(max_length=128)
    level = models.IntegerField(default=1)  # Assume kids start level 1. This field is probably wrong.. need to look into  how to access level

    def __str__(self):
        return self.name

class Level(models.Model):  # TODO Need to find out how to access model ID
    name = models.CharField(max_length=128, unique=True) # E.g. "Level 1"
# Level and MaterialSubject may be optimised... need to consider this
    def __str__(self):
        return self.name

class MaterialSubject(models.Model):
    name = models.CharField(max_length=128, unique=True) # E.g. "Lochs of Scotland"
    level = models.ForeignKey(Level)

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=128, unique=True) # E.g. "Loch Lomond" [attribute not in original ER]
    content = models.CharField(max_length=2000) # E.g. "Loch Lomond is the biggest loch in Scotland..."
    subject = models.ForeignKey(MaterialSubject)

    def __str__(self):
        return self.name

class QuizQuestion(models.Model):   # some sort of Questionid may be needed here
    difficulty = models.IntegerField(default=0) #may need to drop this one
    question = models.CharField(max_length=128, unique=True) # E.g. "What is the biggest loch in Scotland?"
    CorrectAnswer = models.CharField(max_length=128) # E.g. "Loch Lomond"
    incorrectAnswer1 = models.CharField(max_length=128) # E.g "Loch Ness"
    incorrectAnswer2 = models.CharField(max_length=128) # E.g. "Loch Awe"
    incorrectAnswer3 = models.CharField(max_length=128) # E.g. "Loch Katrine"
    subject = models.ForeignKey(MaterialSubject)

    def __str__(self):
        return self.question

# Creates ParentProfile object when creating a new User
@receiver(post_save, sender=User)
def create_parent_profile(sender, instance, created, **kwargs):
    if created:
        ParentProfile.objects.create(user=instance)
# Saves the ParentProfile object when a new User is saved
@receiver(post_save, sender=User)
def save_parent_profile(sender, instance, **kwargs):
    instance.parentprofile.save()
