import requests
from django.shortcuts import render

def home(request):
  #USING APIS
  response=requests.get('https://api.github.com/events')
  data=response.json()
  result=data[0]["id"]

  return render(request, 'templates/index.html', {'result':result})
  

