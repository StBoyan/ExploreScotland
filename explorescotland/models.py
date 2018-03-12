from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class ParentProfile(models.Model):
    GENDER_CHOICES = (
    ('', 'Not specified'),
    ('M', 'Male'),
    ('F', 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default ='')
    birthdate = models.DateField(null=True)

    def __str__(self):
        return self.user.username

class Feedback(models.Model):
    message = models.TextField(null=False)
    date = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(User)

class ChildProfile(models.Model):
    parent = models.ForeignKey(User)
    name = models.CharField(max_length=40, null=False)
    level = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class Level(models.Model):
    number = models.IntegerField(primary_key=True) # E.g. "1"
    topic = models.CharField(max_length=50, unique=True) # E.g. "Glasgow"
    content = models.TextField(null=False) # E.g. "Glasgow is the biggest city in Scotland..."
    numOfQuestions = models.IntegerField(null=False) # How many questions will this level have

    def __str__(self):
        return self.number

class QuizQuestion(models.Model):
    question_id = models.IntegerField(primary_key=True) # E.g. 1,2,3.. Up to number of questions for the relevant Level (not enforced by database)
    question = models.CharField(max_length=128, unique=True) # E.g. "When was University of Glasgow established?"
    correctAnswer = models.CharField(max_length=128) # E.g. "1451"
    incorrectAnswer1 = models.CharField(max_length=128) # E.g "1285"
    incorrectAnswer2 = models.CharField(max_length=128) # E.g. "1613"
    incorrectAnswer3 = models.CharField(max_length=128) # E.g. "1771"
    level = models.ForeignKey(Level)

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
