from django.shortcuts import render

from .forms import Triangle


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
            hypotenuse = round((cath_x**2 + cath_y**2) ** 0.5, 3)
            values_form = Triangle()
    else:
        values_form = Triangle()
    return render(request, 'math_app/triangle.html', {'cath_x': cath_x,
                                                      'cath_y': cath_y,
                                                      'hypotenuse': hypotenuse,
                                                      'values_form': values_form})
