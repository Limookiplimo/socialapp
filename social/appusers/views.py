from django.shortcuts import render, redirect
from .forms import ProfileForm

# Create your views here.
def profile_page(request):
    profile = request.user.profile
    context = {'profile':profile}
    return render(request,'appusers/profile.html',context)

def edit_profile(request):
    form = ProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    context = {'form':form}
    return render(request,'appusers/profile_edit.html', context)
