from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def auth_page(request):
    # return render(request, 'auth.html')
    return HttpResponse("This is the auth page.")