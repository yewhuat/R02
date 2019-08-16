import logging
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.views.generic import (ListView, DetailView, )
from django.shortcuts import render, get_object_or_404,redirect, HttpResponseRedirect

from .forms import UserForm, ProfileForm
from .models import Profile



# Get an instance of a logger
#logger = logging.getLogger(__name__)
logger = logging.getLogger("info_logger")


User = get_user_model()


class ProfileListView(ListView):
    #logging.getLogger("info_logger").info("Logger Trigger ListView")
    logger.info("Logger Trigger ListView")
    template_name = 'profiles/profile_list.html'
    queryset = Profile.objects.all()


class ProfileDetailView(LoginRequiredMixin, DetailView):
    #default template_name = 'profiles/profile_detail.html'
    #logging.getLogger("info_logger").info("Logger Trigger DetailView")
    logger.warning("Logger Trigger DetailView")
    model = Profile
    #fields = ['dob', 'gender', 'tagline', 'description']


# class ProfileUpdateView(LoginRequiredMixin, UpdateView):
#     model = Profile
#     fields = ['dob', 'gender']


@login_required(login_url='/accounts/login/')
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            logger.info("Profile Successfully Updated:{}".format(request.user))
            return HttpResponseRedirect('/profile/')

    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        logger.info("Profile Successfully Loaded:{}".format(request.user))
    return render(request, 'profiles/update.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

