from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
# Create your views here.
def index(request):
    if request.method == 'GET':
        hotel = Hotel.objects.all()
        return render(request, 'hotel/index.html',{
            'hotels': hotel
        })

def imageUpload(request):
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
        else:
            return redirect('success')

    else:
        form = HotelForm
    return render(request, 'hotel/hotel.html',{
        'form': form
    })


def success(request):
    return HttpResponse('You have successfully uploaded!')

@login_required
def contact(request):
    user = User.objects.all()
    return render(request, 'hotel/contact.html',{
        'users': user
    })
