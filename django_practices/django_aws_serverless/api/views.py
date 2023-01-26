from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer

class Dummy(APIView):
    def get(self, request, format=None, *args, **kwargs):
        content = {'test': 'test 1'}
        return Response(content)
