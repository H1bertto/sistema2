from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SignUpForm


# Create your views here.
def login(request):
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("/manage/")
    else:
        form = SignUpForm()

    context = {
        'form': form
    }
    return render(request, 'signup.html', context)


def manage(request):
    return render(request, 'admin.html')
