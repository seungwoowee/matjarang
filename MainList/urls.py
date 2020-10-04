from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    # path('<int:pageid>/', views.contents)
    # path('test/', views.contents)
    path('<int:pageid>/', views.contents)
]
