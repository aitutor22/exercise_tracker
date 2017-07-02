from django import forms
from django.forms import ModelForm, inlineformset_factory, BaseInlineFormSet

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

from .models import Workout, ExerciseSet

#formset example
#https://medium.com/@adandan01/django-inline-formsets-example-mybook-420cc4b6225d
#https://stackoverflow.com/questions/27968417/django-form-with-fields-from-two-different-models
#https://stackoverflow.com/questions/34317157/multiple-django-crispy-forms-in-one-view

#form from scratch
#https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms

class WorkoutForm(ModelForm):
    class Meta:
        model = Workout
        exclude = ()

class ExerciseSetForm(ModelForm):
    class Meta:
        model = ExerciseSet
        exclude = ()

class CustomExerciseSetInlineFormSet(BaseInlineFormSet):
    def clean(self):
        cleaned_data = super().clean()
        print('custom')
        print(cleaned_data)


ExerciseSetFormSet = inlineformset_factory(Workout, ExerciseSet, form=ExerciseSetForm, 
    formset=CustomExerciseSetInlineFormSet, extra=3)