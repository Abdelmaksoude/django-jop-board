from django.shortcuts import render , redirect
from .forms import SignupForm , UserForm , ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login
from .models import Profile
from django.urls import reverse
from django.contrib.auth.models import User , auth , Group
from django.contrib import messages

# Create your views here.

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username , password=password)

        if user is not None:
            auth.login(request , user)
            messages.success(request , 'Forsa Welcomes You...')
            return redirect('/')
        else:
            messages.info(request , 'Regesstriation Invalid')
            return redirect(reverse('accounts:signin'))
    else:
        return render(request , 'accounts/signin.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2']
        is_company = request.POST.get('is_company', False)

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request , 'Email Taken')
                return redirect(reverse('accounts:signup'))
            elif User.objects.filter(username=username).exists():
                messages.info(request , 'Username Token')
                return redirect(reverse('accounts:signup'))
            else:
                user = User.objects.create_user(username=username , email=email , password=password )
                if is_company:
                    company_group, created = Group.objects.get_or_create(name='Company')
                    user.groups.add(company_group)
                    user.save()
                #login user and redirect to the setting page
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                messages.success(request , 'Best Wishes For You in Forsa!')
                return redirect(f'/accounts/profile/{username}')
        else:
            messages.info(request , 'Password Not Matching')
            return redirect(reverse('accounts:signup'))
    else:
        return render(request , 'accounts/signup.html')

@login_required
def profile(request , pk):
    user_object = User.objects.get(username=pk)
    profile = Profile.objects.get(user=user_object)
    return render(request , 'accounts/profile.html' , {'profile':profile})

def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method=='POST':
        userform = UserForm(request.POST , instance=request.user)
        profileform = ProfileForm(request.POST , request.FILES , instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(f'/accounts/profile/{profile}')
    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)
    return render(request , 'accounts/profile_edit.html' , {'userform':userform , 'profileform':profileform})

@login_required(login_url='accounts:signin')
def logout(request):
    auth.logout(request)
    return redirect('/')
