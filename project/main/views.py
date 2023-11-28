from django.shortcuts import render, redirect
from .forms import RegerForm

def index(request):
    form = RegerForm()
    error = ''

    data = {
        'form': form,
        'error': error
    }

    if request.method == 'POST':
        form = RegerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма неверна'

    return render(request, 'main/index.html', data)
