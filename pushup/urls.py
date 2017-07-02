from django.conf.urls import url
from .views import WorkoutListView, WorkoutDetailView, WorkoutCreate, ExerciseSetCreate

app_name = 'pushup'

urlpatterns = [
    url(r'^$', WorkoutListView.as_view(), name='workout-list'),
    url(r'^(?P<pk>\d+)/$', WorkoutDetailView.as_view(), name='workout-detail'),
    url(r'^exercise_set/add/$', ExerciseSetCreate.as_view(), name='exercise-set-add'),
    url(r'^add/$', WorkoutCreate.as_view(), name='workout-add'),
]
