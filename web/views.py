from django.shortcuts import render

# Create your views here.


def index(request):
    """
        Render the index page
    """
    return render(request, 'index.html', {})

# ACTIVITIES


def a0(request):
    """
        Render the A0 page
    """
    return render(request, 'outputs/a/a0.html', {})


def a1(request):
    """
        Render the A1 page
    """
    return render(request, 'outputs/a/a1.html', {})


def a2(request):
    """
        Render the A2 page
    """
    return render(request, 'outputs/a/a2.html', {})


def a3(request):
    """
        Render the A3 page
    """
    return render(request, 'outputs/a/a3.html', {})


def a4(request):
    """
        Render the A4 page
    """
    return render(request, 'outputs/a/a4.html', {})


def a5(request):
    """
        Render the A5 page
    """
    return render(request, 'outputs/a/a5.html', {})

# GUIDE QUESTIONS


def g1(request):
    """
        Render the G1 page
    """
    return render(request, 'outputs/g/g1.html', {})


def g2(request):
    """
        Render the G2 page
    """
    return render(request, 'outputs/g/g2.html', {})


def g3(request):
    """
        Render the G3 page
    """
    return render(request, 'outputs/g/g3.html', {})

# REFLECTIONS


def r1(request):
    """
        Render the R1 page
    """
    return render(request, 'outputs/r/r1.html', {})


def r2(request):
    """
        Render the R2 page
    """
    return render(request, 'outputs/r/r2.html', {})


def r3(request):
    """
        Render the R3 page
    """
    return render(request, 'outputs/r/r3.html', {})


def r4(request):
    """
        Render the R4 page
    """
    return render(request, 'outputs/r/r4.html', {})


def r5(request):
    """
        Render the R4 page
    """
    return render(request, 'outputs/r/r5.html', {})
