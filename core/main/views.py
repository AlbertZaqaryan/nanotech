from django.shortcuts import render, redirect
from .models import Slider, Contact, About, Team, Info

def index(request):
    slider_list = Slider.objects.all()
    return render(request, 'index.html', {
        'slider_list':slider_list
    })


def about(request):
    about = About.objects.first()
    team_list = Team.objects.all()
    return render(request, 'about.html', {
        'about':about,
        'team_list':team_list
    })


def contact(request):
    info = Info.objects.first()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, text=message)
        return redirect('contact')
    return render(request, 'contact.html', {
        'info':info
    })