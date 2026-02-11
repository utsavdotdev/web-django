from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Registration
from django.contrib.auth.hashers import make_password


def registration_form(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            registration = Registration(
                name=data['name'],
                email=data['email'],
                password=make_password(data['password']),
            )
            registration.save()
            return redirect('registration:form')
    else:
        form = RegistrationForm()

    return render(request, 'registration/form.html', {'form': form})
