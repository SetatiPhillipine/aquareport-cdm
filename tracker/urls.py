from django.urls import path
from . import views

urlpatterns = [
    path('reports/', views.all_reports, name='all_reports'),
    path('stats/', views.stats, name='stats'),
    path('update-reports/', views.update_reports, name='update_reports'),
]