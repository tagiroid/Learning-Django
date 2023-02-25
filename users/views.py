from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    # registration new user
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        # working with filled form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # login and redirecting to homepage
            login(request, new_user)
            return redirect('learning_logs:index')

    # show empty or invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)
