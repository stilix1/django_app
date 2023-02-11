from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from client.forms import ProfileForm


def profile(request):
    template = 'client/account.html'
    profile_form = ProfileForm
    return render(request,
                  template,
                  context={
                    'profile': profile_form
                  })
