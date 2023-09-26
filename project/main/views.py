from django.shortcuts import render, redirect
from .forms import RegerForm

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = ReferenceError(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма неверна'

    form = RegerForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/index.html', data)
