from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render

from .forms import RegistrationForm


def register(request):
    if request.user.is_authenticated:
        return redirect('accounts:dashboard')

    form = RegistrationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        regular_users, _ = Group.objects.get_or_create(name='Regular user')
        user.groups.add(regular_users)
        login(request, user)
        return redirect('accounts:dashboard')

    return render(request, 'accounts/register.html', {'form': form})


@login_required
def dashboard(request):
    role = 'Administrator' if request.user.is_staff else 'Regular user'
    return render(request, 'accounts/dashboard.html', {'role': role})