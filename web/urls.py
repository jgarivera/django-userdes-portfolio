"""
    Class for defining URL routes
"""
from django.urls import path

from . import views

app_name = 'web'
urlpatterns = [
    path('', views.index, name='index'),

    # Activities
    path('outputs/a0', views.a0, name='a0'),
    path('outputs/a1', views.a1, name='a1'),
    path('outputs/a2', views.a2, name='a2'),
    path('outputs/a3', views.a3, name='a3'),
    path('outputs/a4', views.a4, name='a4'),

    # Guide Questions
    path('outputs/g1', views.g1, name='g1'),
    path('outputs/g2', views.g2, name='g2'),
    path('outputs/g3', views.g3, name='g3'),

    # Reflections
    path('outputs/r1', views.r1, name='r1'),
    path('outputs/r2', views.r2, name='r2'),
    path('outputs/r3', views.r3, name='r3'),
    path('outputs/r4', views.r4, name='r4'),
    path('outputs/r5', views.r5, name='r5'),
]
