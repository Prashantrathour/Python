from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def postcreation(request):
    if request.method=="post":
         username=request.get("username")
         caption=request.get("caption")
         print(username,caption)
        
    return render(request, "index.html")
