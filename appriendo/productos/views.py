from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def inicio(request):
    return render(request, 'productos/inicio.html')

class CustomLoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True

@login_required
def dashboard(request):
    return render(request, "dashboard.html")
