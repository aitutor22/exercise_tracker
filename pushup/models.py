from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone 
from django.core.urlresolvers import reverse

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Workout(models.Model):
    profile = models.ForeignKey(
            'Profile', on_delete=models.CASCADE, blank=False
        )

    created = models.DateField(default=timezone.now)

    def __str__(self):
        return '{} - {}'.format(self.profile.user.username, self.created.strftime('%B %d, %Y'))

    def get_absolute_url(self):
        return reverse('pushup:workout-detail', kwargs={'pk': self.pk})

class ExerciseSet(models.Model):
    EXERCISE_TYPE_CHOICES = (
        ('pushup', 'Push Up'),
        ('situp', 'Sit-up')
    )

    workout = models.ForeignKey(
            'Workout', on_delete=models.CASCADE, related_name='exercise_sets'
        )

    repetitions = models.PositiveIntegerField(null=True, blank=True)
    exercise_type = models.CharField(max_length=100, choices=EXERCISE_TYPE_CHOICES, null=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.exercise_type, self.repetitions)
