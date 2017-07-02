from django.conf.urls import url
from .views import WorkoutListView, WorkoutDetailView, WorkoutCreate, ExerciseSetCreate, WorkoutUpdate

app_name = 'pushup'

urlpatterns = [
    url(r'^$', WorkoutListView.as_view(), name='workout-list'),
    url(r'^(?P<pk>\d+)/$', WorkoutDetailView.as_view(), name='workout-detail'),
    url(r'^add/$', WorkoutCreate.as_view(), name='workout-add'),
    url(r'^(?P<pk>\d+)/edit/$', WorkoutUpdate.as_view(), name='workout-update')
]
