from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import Movie, Comment
from .forms import CommentForm


class MovieListView(ListView):
    model = Movie
    paginate_by = 4  # if pagination is desired
    template_name = 'moviegrid.html'

    def get_context_data(self, **kwargs):
        moviesAll = Movie.objects.all()
        statusRA = Movie.objects.filter(status='RA')
        statusMW = Movie.objects.filter(status='MW')
        statusTR = Movie.objects.filter(status='TR')
        contexts = {
            'moviesAll':moviesAll,
            'statusRA': statusRA,
            'statusMW': statusMW,
            'statusTR': statusTR,

        }
        return contexts


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'moviesingle.html'
    form = CommentForm

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()

            return redirect(reverse('detail_list', kwargs={
                'pk': post.pk,
            }))
            # return render(request,'movie_detail.html')

    def get_context_data(self, **kwargs):
        post_comments = Comment.objects.all().filter(post=self.object.id)
        context = super().get_context_data(**kwargs)
        context.update({
            'form': self.form,
            'post_comments': post_comments,
        })
        return context


class SearchResultsView(ListView):
    model = Movie
    template_name = 'search/search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        object_list = Movie.objects.filter(
            Q(title__icontains=query) | Q(status__icontains=query)
        )
        return object_list



def latest_added(request):
    statusRA = Movie.objects.filter(status='RA')
    context = {
        'ra':statusRA,
        }
    return render (request,'site_pages/latest_added.html',context)


def most_watched(request):
    statusMW = Movie.objects.filter(status='MW')
    context = {
        'mw':statusMW,
        }
    return render (request,'site_pages/most_watched.html',context)


def top_rated(request):
    statusTR = Movie.objects.filter(status='TR')
    context = {
        'tr':statusTR,
        }
    return render (request,'site_pages/top_rated.html',context)


def insta(request):

    context = {
        
        }
    return render (request,'insta.html',context)


def test(request):
    
    return render (request,'test.html')