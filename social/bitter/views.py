from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Profile, Bit
from .forms import BitForm, SignUpForm, ProfilePicForm, UpdateForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response

def home(request):
    if request.user.is_authenticated:
        form = BitForm(request.POST or None, request.FILES or None)
        # print(form.bit_image)
        if request.method == "POST":
            if form.is_valid():
                bit = form.save(commit=False)
                bit.user = request.user
                bit.save()
                messages.success(request, ("Your Bit has been posted :)"))
                return redirect('home')
        following_ids = request.user.profile.follows.values_list('user_id', flat=True)
        # bits = Bit.objects.all().order_by("-created_at")
        bits = Bit.objects.filter(user__id__in=following_ids).order_by('-created_at')
        return render(request, 'home.html',{"bits":bits, "form":form})
    else:
        bits = Bit.objects.all().order_by("-created_at")
        return render(request, 'home.html',{"bits":bits})

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'profile_list.html', {"profiles":profiles})
    else:
        messages.success(request, ("You must be logged in to view this page"))
        return redirect('home')
    
# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        bits = Bit.objects.filter(user_id=pk).order_by("-created_at")

        #Post Form logic
        if request.method == "POST":
            #Get current user
            current_user_profile = request.user.profile
            #Get form data
            action = request.POST['follow']
            # Decide to follow or unfollow
            if action == "unfollow":
                current_user_profile.follows.remove(profile)
            elif action == "follow":
                current_user_profile.follows.add(profile)
            # Save the profile
            current_user_profile.save()
        return render(request, "profile.html", {"profile":profile, "bits":bits})
    else:
        messages.success(request, ("You must be logged in to view this page"))
        return redirect('home')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = authenticate(request, username=username, password=password, email=email)
        if user is not None and email == user.email:
            login(request, user)
            messages.success(request, ("You have been logged in. Get Bits"))
            return redirect('home')
        else:
            messages.success(request, ("There was an error logging in. Please, try again"))
            return redirect('login')
    else:
        return render(request, "login.html", {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out. See you later"))
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']

            #Log in user
            user = authenticate(username=username, password=password, email=email)
            login(request, user)
            messages.success(request, ("You have successfully registered. Welcome"))
            return redirect('home')
    return render(request, "register.html", {'form': form})

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        profile_user = Profile.objects.get(user_id=request.user.id)           
        user_form = UpdateForm(request.POST or None, request.FILES or None, instance=current_user)
        profile_form = ProfilePicForm(request.POST or None, request.FILES or None, instance=profile_user)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            login(request, current_user)
            messages.success(request, ("Your profile has been updated."))
            return redirect('home')            
        return render(request, "update_user.html", {'user_form':user_form, 'profile_form':profile_form})
    else:
        messages.success(request, ("You must be logged do access this page."))
        return redirect('home')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)  # Mantém o usuário logado após a alteração
            messages.success(request, "Your password has been changed successfully.")
            return redirect('home')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = PasswordChangeForm(user=request.user)
    
    return render(request, 'change_password.html', {'form': form})

def bit_like(request, pk):
    if request.user.is_authenticated:
        bit = get_object_or_404(Bit, id=pk)
        if bit.likes.filter(id=request.user.id):
            bit.likes.remove(request.user)
        else:
            bit.likes.add(request.user)
        return redirect('home')
    else:
        messages.success(request, ("You must be logged in to like posts"))
        return redirect('home')
    
def delete_bit(request, pk):
    if request.user.is_authenticated:
        bit = get_object_or_404(Bit, id=pk)
        if request.user.username == bit.user.username:
            bit.delete()
            messages.success(request, ("The post has been deleted"))    
            return redirect(request.META.get("HTTP_REFERER"))
        else:
            messages.success(request, ("That is not your post"))    
            return redirect('home')
    else:
        messages.success(request, ("You must be logged in to delete posts"))
        return redirect(request.META.get("HTTP_REFERER"))

def edit_bit(request, pk):
    if request.user.is_authenticated:
        bit = get_object_or_404(Bit, id=pk)
        if request.user.username == bit.user.username:
            form = BitForm(request.POST or None, request.FILES or None, instance=bit)
            if request.method == "POST":
                if form.is_valid():
                    bit = form.save(commit=False)
                    bit.user = request.user
                    bit.save()
                    messages.success(request, ("Your Bit has been updated)"))
                    return redirect('home')
            else:
                return render(request, "edit_bit.html", {'form':form, 'bit': bit})
        else:
            messages.success(request, ("That is not your post"))    
            return redirect('home')
    else:
        messages.success(request, ("You must be logged in to update posts"))
        return redirect('home')