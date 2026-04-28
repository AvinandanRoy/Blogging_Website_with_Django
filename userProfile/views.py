from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from userProfile.forms import UserProfileForm
from django.contrib.auth.decorators import login_required

from userProfile.models import UserProfile

# Create your views here.
@login_required(login_url="login")
def profile(req):
    user = req.user
    try:
        profile = req.user.userprofile
    except:
        profile = None
    
    context ={
        'user': user,
        'profile': profile,
    }
    
    return render(req, "profile/userProfile.html", context  )


# Only Logged-in User Can Edit Own Profile
@login_required(login_url="login")
def editUserProfile(req):
    user_profile = req.user.userprofile   # 🔥 current logged-in user profile

    if req.method == 'POST':
        form = UserProfileForm(req.POST,req.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = UserProfileForm(instance=user_profile)

    context = {
        'form': form,
    }
    return render(req, "profile/editUserProfile.html", context)


def view_user_profile(req , username):
    user = get_object_or_404(User , username = username)
    
    try:
        profile = user.userprofile
    except UserProfile.DoesNotExist:
        profile = None
    context ={
        "user" : user,
        'profile': profile ,
    }
    return render(req , "profile/view_user_profile.html", context)
