from django.urls import path

from . import views
from .views import MovieListView, MovieDetailView, SearchResultsView

urlpatterns = [
    path('', MovieListView.as_view(), name='movie_list'),
    path('<int:pk>', MovieDetailView.as_view(), name='detail_list'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('horijiy_kinolar', views.horijiy_kinolar, name='horijiy_kinolar'),
    path('milliy_filmlar', views.milliy_filmlar, name='milliy_filmlar'),
    path('multfilmla', views.multfilmla, name='multfilmla'),
    path('insta', views.insta, name='insta'),
    path('test', views.test, name='test'),
]
