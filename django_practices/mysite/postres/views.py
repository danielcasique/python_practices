from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader

# Create your views here.

def primera(request):
    context = {        
    }
    template = loader.get_template('postres/primera.html')
    return HttpResponse(template.render(context, request))