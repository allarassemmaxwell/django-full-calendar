from django.urls import path
from .views import *
urlpatterns = [
	path('', home_view, name="home"),
	path('calendar/', calendar, name="calendar"),
	path('add_event/', add_event, name="add_event"),
	path('update/', update, name="update"),
	path('remove/', remove, name="remove"),
	path('all_events/', all_events, name="all_events"),

	path('event/', event, name="event"),
]




