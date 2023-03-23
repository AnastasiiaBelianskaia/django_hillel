from django.shortcuts import get_object_or_404, redirect, render

from .forms import PersonForm, Triangle
from .models import Person as PersonModel


def index(request):
    return render(request, 'math_app/index.html')


def triangle(request):
    cath_x = None
    cath_y = None
    hypotenuse = None

    if "submit" in request.GET:
        values_form = Triangle(request.GET)
        if values_form.is_valid():
            cath_x = values_form.cleaned_data['cath_x']
            cath_y = values_form.cleaned_data['cath_y']
            hypotenuse = round((cath_x ** 2 + cath_y ** 2) ** 0.5, 3)
            values_form = Triangle()
    else:
        values_form = Triangle()
    return render(request, 'math_app/triangle.html', {'cath_x': cath_x,
                                                      'cath_y': cath_y,
                                                      'hypotenuse': hypotenuse,
                                                      'values_form': values_form})


def create_entry(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return redirect('math_app:created_entry', pk=new_user.id)
    else:
        form = PersonForm()
    return render(request, 'math_app/create_entry.html', {'user_form': form})


def created_entry(request, pk):
    user_instance = get_object_or_404(PersonModel, id=pk)
    return render(request, 'math_app/after_creating_entry.html', {'user_instance': user_instance})


def edit_entry(request, pk):
    user_instance = get_object_or_404(PersonModel, id=pk)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=user_instance)
        if form.is_valid():
            edited_user = form.save()
            return redirect('math_app:edited_entry', pk=edited_user.id)
    else:
        form = PersonForm(instance=user_instance)
    return render(request, 'math_app/edit_entry.html', {'user_instance': user_instance, 'user_edit_form': form})


def edited_entry(request, pk):
    user_instance = get_object_or_404(PersonModel, id=pk)
    return render(request, 'math_app/after_editing_entry.html', {'user_instance': user_instance})
