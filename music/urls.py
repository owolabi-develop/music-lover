from django.urls import path,include
from . import views
app_name = "musiclovers"
urlpatterns = [
    path('',views.baseMusic,name='Base-music'),
    path('Search/',views.music_search,name="music-search")
]
