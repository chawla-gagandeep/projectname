from django.shortcuts import render, redirect
from .models import User
from .forms import UserInputForm

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})


def user_input(request):
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-list')  # Redirect to a page displaying the user list
    else:
        form = UserInputForm()
    return render(request, 'user_input.html', {'form': form})