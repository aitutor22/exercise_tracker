from django.contrib import admin
from .models import Profile, ExerciseSet


class ExerciseSetAdmin(admin.ModelAdmin):
	list_display = ('profile', 'repetitions', 'exercise_type', 'created')

admin.site.register(Profile)
admin.site.register(ExerciseSet, ExerciseSetAdmin)
