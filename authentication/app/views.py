from django.shortcuts import render,HttpResponseRedirect
from app.forms import SignUpForm,EditUserProfileForm,EditAdminProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User
# Create your views here.

#signup view function
def sign_up(request):

    if request.method=='POST':
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,'account created successfully')
            fm.save()
    else:        
     fm=SignUpForm()
    return render(request,'app.html',{'form':fm})



def user_login(request):
    if request.method=="POST":
      fm=AuthenticationForm(request=request,data=request.POST)
      if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                messages.success(request,'Account logged in successfully')
                return HttpResponseRedirect('/profile/')
    else:
       fm=AuthenticationForm()
         
   
    return render(request,'userlogin.html',{'form':fm})

def user_profile(request):
    if request.user.is_authenticated:
      if request.method=="POST":  
        if request.user.is_superuser==True:
           fm=EditAdminProfileForm(request.POST,instance=request.user)
           user=User.objects.all()
        else:
           fm=EditUserProfileForm(request.POST,instance=request.user)
        if fm.is_valid():
           messages.success(request,'profile updated successfully')
           fm.save()
      else:           
         if request.user.is_superuser==True:
            fm=EditAdminProfileForm(instance=request.user)
            users=User.objects.all()
         else:
            fm=EditUserProfileForm(instance=request.user)
      return render(request,'profile.html',{'name':request.user,'form':fm,'users':users}) 
    else:
        return HttpResponseRedirect('/login/')
#user logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
    
def user_change_pass(request):
    if request.user.is_authenticated: 
     if request.method=="POST":
      fm=PasswordChangeForm(request=request.user,data=request.POST)
      if fm.is_valid():
            fm.save()
            update_session_auth_hash(request,fm.user)
            messages.success(request,'password changed successfully')
            return HttpResponseRedirect('/profile/')
     else:
        fm=PasswordChangeForm(user=request.user)
     return render(request,'changepass.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')