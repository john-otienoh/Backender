from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required
def index(request):
    return render(request,'account/index.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_data_has_error = False
        if User.objects.filter(username=username).exists():
            user_data_has_error = True
            # messages.error(request, "Username Already Exists")

        if User.objects.filter(email=email).exists():
            user_data_has_error = True
            # messages.error(request, "Email Already Exists")

        if len(password) < 8:
            user_data_has_error = True
            # messages.error(request, "Password must be atleast 8 Characters")


        if user_data_has_error:
            return redirect('account:register')
        else:
            new_user = User.objects.create_user(
                email=email, 
                username=username,
                password=password,
            )
            # messages.success(request, "Account created successfully, Login Now")
            return redirect('account:login')
    return render(request, 'account/register.html')
