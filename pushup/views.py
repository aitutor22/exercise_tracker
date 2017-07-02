from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db import transaction
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import ValidationError

from .models import Workout, ExerciseSet
from .forms import ExerciseSetFormSet, WorkoutForm, ExerciseSetForm

# Example of Django class based views with inline formset
# https://gist.github.com/neara/6209563
# https://github.com/timhughes/django-cbv-inline-formset
# https://stackoverflow.com/questions/1113047/creating-a-model-and-related-models-with-inline-formsets
# https://stackoverflow.com/questions/15161982/how-to-submit-a-form-and-formset-at-the-same-time

#dynamically adding forms
#http://stellarchariot.com/blog/2011/02/dynamically-add-form-to-formset-using-javascript-and-django/

class WorkoutListView(ListView):
    model = Workout

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Exercise Tracker - Index Page'
        return context

class WorkoutDetailView(DetailView):
    model = Workout

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class WorkoutCreate(CreateView):
    model = Workout
    fields = ['profile', 'created']
    template_name = 'pushup/workout_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['workout_form'] = WorkoutForm()
        context['exercise_set_form'] = ExerciseSetFormSet()

        return context

    def post(self, request, *args, **kwargs):
        workout_form = WorkoutForm(request.POST)
        formset = ExerciseSetFormSet(request.POST)

        if workout_form.is_valid() and formset.is_valid():
            with transaction.atomic():
                workouts_saved = 0
                workout = workout_form.save()
                           
                for exercise_set_form in formset:
                    exercise_set = exercise_set_form.save(commit=False)

                    if exercise_set.repetitions == None or exercise_set.exercise_type == None:
                        continue

                    exercise_set.workout = workout
                    exercise_set.save()
                    workouts_saved += 1

                if workouts_saved == 0:
                    raise ValidationError('No workouts are valid')

                return HttpResponseRedirect(reverse_lazy('pushup:workout-detail', kwargs={'pk': workout.pk}))
        else:
            raise Http404 

class WorkoutUpdate(UpdateView):
    model = Workout
    fields = ['profile', 'created']
    template_name = 'pushup/workout_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['workout_form'] = WorkoutForm(instance=self.object)
        context['exercise_set_form'] = ExerciseSetFormSet(instance=self.object)
        return context

    def post(self, request, *args, **kwargs):
        workout_form = WorkoutForm(request.POST, instance=self.get_object())
        formset = ExerciseSetFormSet(request.POST, instance=self.get_object())

        if workout_form.is_valid() and formset.is_valid():
            with transaction.atomic():
                workouts_saved = 0
                workout = workout_form.save()
                           
                for exercise_set_form in formset:
                    exercise_set = exercise_set_form.save(commit=False)

                    if exercise_set.repetitions == None or exercise_set.exercise_type == None:
                        continue

                    exercise_set.workout = workout
                    exercise_set.save()
                    workouts_saved += 1

                if workouts_saved == 0:
                    raise ValidationError('No workouts are valid')

                return HttpResponseRedirect(reverse_lazy('pushup:workout-detail', kwargs={'pk': workout.pk}))
        else:
            raise Http404     

class ExerciseSetCreate(CreateView):
    model = ExerciseSet
    fields = ['repetitions', 'exercise_type']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
