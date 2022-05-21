from django.urls import path

from . import views
from .views import MovieListView, MovieDetailView, SearchResultsView

urlpatterns = [
    path('', MovieListView.as_view(), name='movie_list'),
    path('<int:pk>', MovieDetailView.as_view(), name='detail_list'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('latestadded', views.latest_added, name='latestadded'),
    path('most_watched', views.most_watched, name='most_watched'),
    path('top_rated', views.top_rated, name='top_rated'),
    path('insta', views.insta, name='insta'),
    path('test', views.test, name='test'),
]
