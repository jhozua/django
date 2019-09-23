from django.urls import path
from .views import MovieList
from .views import SignUp
from .views import MoviesRecommendedList


urlpatterns = [
    path('signup/', SignUp.as_view()),
    path('movie/', MovieList.as_view(), name='movie_list'),
    path('movies_recommended/', MoviesRecommendedList.as_view(), name='movie_list_recommended')
]
