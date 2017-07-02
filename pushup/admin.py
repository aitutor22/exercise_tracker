from django.contrib import admin
from .models import Profile, Workout, ExerciseSet

from . import forms

class ExerciseSetInline(admin.TabularInline):
    model = ExerciseSet

class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('profile', 'created')
    inlines = [
        ExerciseSetInline
    ]

admin.site.register(Profile)
admin.site.register(Workout, WorkoutAdmin)
admin.site.register(ExerciseSet)
