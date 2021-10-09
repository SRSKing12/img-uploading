from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib import messages
from .forms import createUserForm, UserinfoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from .models import User, Userinfo

# Create your views here.
def index(request):
    return render(request, 'index.html')

def sout(request):
    logout(request)
    return render(request, 'index.html')

def sgin(request):
    if request.method == "POST":
        # check if user has entered correct credientials
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("sginpg")

        else:
            # No backend authenticated the credentials
            messages.error(request, 'Invalid username or password!')    
            return render(request, 'sgin.html')

    return render(request, 'sgin.html')

def regst(request):
    if request.method == 'POST':
        form = createUserForm(request.POST)
        profile_form = UserinfoForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'User Created successfully!')   
            return redirect("sin") 

    else:
        form = createUserForm()
        profile_form = UserinfoForm()

    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'register.html', context)

@login_required(login_url = 'sin')
def sginpg(request):
    return render(request, 'sginpg.html')

@login_required(login_url = 'sin')
def change_pass(request):
    if request.method == 'POST':
        fm = PasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Password changed successfully!')    
            update_session_auth_hash(request, fm.user)
            return redirect("sginpg")
    else:
        fm = PasswordChangeForm(user = request.user)
            
    return render(request, 'change_pass.html', {'form':fm})

def update_data(request):
    this_usr = request.user
    usr_inf = Userinfo.objects.get(user = request.user)

    if request.method == "POST":
        fname = request.POST.get('fname')
        phnum = request.POST.get('phnum')
        email = request.POST.get('email')
        state = request.POST.get('state')
        addres = request.POST.get('addres')

        if len(request.FILES) != 0:
            # os.remove(usr_inf.image.path)
            usr_inf.image = request.FILES['img']

        usr_inf.full_Name = fname
        usr_inf.phone = phnum
        usr_inf.state = state
        usr_inf.address = addres
        usr_inf.save()
        
        this_usr.email = email
        this_usr.save()
        messages.success(request, 'Data Updated Successfully!') 
        return redirect("sginpg")

    usr_dat = {
        "usr_info" : usr_inf,
        "my_usr_inf" : this_usr
    }
    return render(request, 'usr_edit.html', usr_dat)