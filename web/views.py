from django.shortcuts import render

# Create your views here.


def index(request):
    """
        Render the index page
    """
    return render(request, 'index.html', {})


def a0(request):
    """
        Render the A1 page
    """
    return render(request, 'outputs/a/a0.html', {})


def a1(request):
    """
        Render the A1 page
    """
    return render(request, 'outputs/a/a1.html', {})


def g1(request):
    """
        Render the G1 page
    """
    return render(request, 'outputs/g/g1.html', {})


def r1(request):
    """
        Render the G1 page
    """
    return render(request, 'outputs/r/r1.html', {})


def r2(request):
    """
        Render the G1 page
    """
    return render(request, 'outputs/r/r2.html', {})


def r3(request):
    """
        Render the G1 page
    """
    return render(request, 'outputs/r/r3.html', {})
