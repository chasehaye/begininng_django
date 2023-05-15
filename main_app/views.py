from typing import Any, Dict
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import LocationForm

from .models import Finch, Feed

# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def finchs_index(request):
    finchs = Finch.objects.all()
    return render(request, 'finchs/index.html', {
        'finchs': finchs
    })
def finchs_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    location_form = LocationForm()
    id_list = finch.feeds.all().values_list('id')
    feeds_finch_doesnt_have = Feed.objects.exclude(id__in=id_list)
    return render(request, 'main_app/detail.html', {
        'finch': finch,
        'location_form': location_form,
        'feeds_finch_doesnt_have': feeds_finch_doesnt_have
    })
class FinchList(ListView):
    model = Finch
class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'breed', 'age', 'length']
class FinchUpdate(UpdateView):
    model = Finch
    fields = ['name', 'breed', 'age', 'length']
class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finchs'
def add_location(request, finch_id):
    form = LocationForm(request.POST)
    if form.is_valid():
        new_location = form.save(commit = False)
        new_location.finch_id = finch_id
        new_location.save()
    return redirect('detail', finch_id=finch_id)
class FeedList(ListView):
  model = Feed
class FeedDetail(DetailView):
  model = Feed
class FeedCreate(CreateView):
  model = Feed
  fields = '__all__'
class FeedUpdate(UpdateView):
  model = Feed
  fields = ['name', 'type']
class FeedDelete(DeleteView):
  model = Feed
  success_url = '/feeds'
def assoc_feed(request, finch_id, feed_id):
    Finch.objects.get(id=finch_id).feeds.add(feed_id)
    return redirect('detail', finch_id=finch_id)

def unassoc_feed(request, finch_id, feed_id):
    Finch.objects.get(id=finch_id).feeds.remove(feed_id)
    return redirect('detail', finch_id=finch_id)