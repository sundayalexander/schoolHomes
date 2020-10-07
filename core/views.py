from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.shortcuts import render, get_object_or_404, redirect
from subdomains.utils import reverse

from core.forms import UserForm
from django.contrib.auth import authenticate, login as auth_login, logout


# Index view
from core.models import Domain


def index(request):
    try:
        domain = Domain.objects.get(domain=request.get_host())
        return render(request, 'school.html', {'school': domain.user})
    except:
        get_object_or_404(Site, domain=request.get_host())
        return render(request, 'index.html', {'subd': request.subdomain})


def authorize(request):
    return redirect('{}?token={}'.format(reverse('simple-sso-authorize'), request.GET['token']))

# Register view
def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            school = form.save()
            return redirect(reverse('school', subdomain=school.username))

    return render(request, 'register.html', {'form': form})


# Login view
def login(request):
    print(request.GET)
    if request.method == 'POST':
        print(request.POST)
        user = {'username': request.POST.get('username'),
         'password': request.POST.get('password')}
        user = authenticate(request, **user)
        if user is not None:
            auth_login(request, user)
            return redirect(request.GET.get('next'))
    print(request.user)
    if request.user.is_authenticated:
        return redirect('index')

    return render(request, 'login.html')



def school(request):
    school = get_object_or_404(User, username=request.subdomain)
    return render(request, 'school.html', {'school': school})


# Register view
def update(request):
    school = get_object_or_404(User, username=request.subdomain)
    form = UserForm(instance=school)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=school)
        if form.is_valid():
            school = form.save()
            return redirect(reverse('school', subdomain=school.username))

    return render(request, 'update.html', {'form': form})
