from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)
from . import models

class IndexView(TemplateView):
  template_name = 'index.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['injectme'] = 'BASIC INJECTION!'
    return context

class SchoolListView(ListView):
  context_object_name = 'schools' # use this if you want to give a custom name to the generated list
  model = models.School
  # it generates school_list by default

class SchoolDetailView(DetailView):
  context_object_name = 'school_detail' # use this if you want to give a custom name to the generated detail
  model = models.School
  template_name = 'basic_app/school_detail.html'
  # it generates school by default

class SchoolCreateView(CreateView):
  fields = ('name', 'principal', 'location')
  model = models.School

class SchoolUpdateView(UpdateView):
  fields = ('name', 'principal')
  model = models.School

class SchoolDeleteView(DeleteView):
  model = models.School
  success_url = reverse_lazy('basic_app:list')
