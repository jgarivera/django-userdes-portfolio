from django.shortcuts import render

# Create your views here.


def index(request):
    """
        Render the index page
    """
    learnings = [
        {
            'img': 'l1.png'
        },
        {
            'img': 'l2.png'
        },
        {
            'img': 'l3.png'
        },
        {
            'img': 'l4.png'
        },
        {
            'img': 'l5.png'
        },
        {
            'img': 'l6.png'
        },
        {
            'img': 'l7.png'
        },
        {
            'img': 'l8.png'
        },
        {
            'img': 'l9.png'
        }
    ]
    context = {'learnings': learnings}
    return render(request, 'index.html', context)

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


def a6(request):
    """
        Render the A6 page
    """
    brandseen_imgs = ['image--001.jpg', 'image--002.jpg', 'image--003.jpg', 'image--004.jpg', 'image--005.jpg',
                      'image--006.jpg', 'image--007.jpg', 'image--008.jpg', 'image--009.jpg', 'image--010.jpg']

    bwt_imgs = ['image--011.jpg', 'image--012.jpg', 'image--013.jpg', 'image--014.jpg',
                'image--015.jpg', 'image--016.jpg', 'image--017.jpg', 'image--018.jpg', 'image--019.jpg', 'image--020.png', 'image--021.jpg']

    context = {'brandseen_imgs': brandseen_imgs, 'bwt_imgs': bwt_imgs}

    return render(request, 'outputs/a/a6.html', context)

def a7(request):
    """
        Render the A7 page
    """
    return render(request, 'outputs/a/a7.html', {})

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
        Render the R5 page
    """
    return render(request, 'outputs/r/r5.html', {})

def r6(request):
    """
        Render the R6 page
    """
    return render(request, 'outputs/r/r6.html', {})
