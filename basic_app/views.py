from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

class VBView(View):
  def get(self, request):
    return HttpResponse('CLASE BASE VIEWS ARE COOL!')
