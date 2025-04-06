from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from educat.forms import AuthForm , ChangerAuthForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth import update_session_auth_hash
from educat.models import Enseignant
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.user.is_authenticated:
        return redirect("educat:home")
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                try:
                    enseignant = Enseignant.objects.get(user=user)
                    if enseignant.is_first_login:
                        return redirect('educat:change_password')
                except Enseignant.DoesNotExist:
                    pass 

                return redirect('educat:home')  
            else:
                form.add_error(None, "Identifiants invalides")
    else:
        form = AuthForm()

    context = {
        'form': form
    }
    return render(request, 'auth/login.html', context)

@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = ChangerAuthForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['new_password']
            request.user.set_password(new_password)
            request.user.save()
            update_session_auth_hash(request, request.user)
            try:
                enseignant = Enseignant.objects.get(user=request.user)
                enseignant.update_first_login_status()  
            except Enseignant.DoesNotExist:
                pass  
            return redirect('educat:home')  
    else:
        form = ChangerAuthForm()

    return render(request, 'auth/change_password.html', {'form': form})

@login_required
def logout_views(request):
    logout(request)
    return HttpResponseRedirect('/login/')


