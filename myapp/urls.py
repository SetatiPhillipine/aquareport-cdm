from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='myapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('report/', views.report_fault, name='report_fault'),
    path('personas/', views.personas, name='personas'),
    path('my-reports/', views.my_reports, name='my_reports'),
    
    # Admin URLs
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-update/<int:report_id>/', views.admin_update_report, name='admin_update_report'),
    path('admin-delete/<int:report_id>/', views.admin_delete_report, name='admin_delete_report'),
]