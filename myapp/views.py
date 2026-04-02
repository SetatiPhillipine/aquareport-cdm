from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import WaterFaultReport

# Helper function to check if user is admin
def is_admin(user):
    return user.is_staff or user.is_superuser

def home(request):
    # Show approved and resolved reports to public
    reports = WaterFaultReport.objects.filter(status__in=['approved', 'resolved']).order_by('-submitted_at')
    total_reports = reports.count()
    pending = WaterFaultReport.objects.filter(status='pending').count()
    resolved = WaterFaultReport.objects.filter(status='resolved').count()
    
    return render(request, 'myapp/home.html', {
        'total_reports': total_reports,
        'pending': pending,
        'resolved': resolved,
    })

def about(request):
    return render(request, 'myapp/about.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created! Now you can report faults.')
            return redirect('report_fault')
    else:
        form = UserCreationForm()
    return render(request, 'myapp/signup.html', {'form': form})

@login_required(login_url='/login/')
def report_fault(request):
    if request.method == 'POST':
        report = WaterFaultReport.objects.create(
            user=request.user,
            name=request.POST['name'],
            gender=request.POST.get('gender', 'male'),
            phone=request.POST.get('phone', ''),
            location=request.POST['location'],
            fault_type=request.POST.get('fault_type', ''),
            description=request.POST['description'],
            status='pending',
        )
        messages.success(request, 'Your report has been submitted! An admin will review it shortly.')
        return redirect('my_reports')
    return render(request, 'myapp/report.html')

def personas(request):
    # Show approved and resolved reports for personas
    reports = WaterFaultReport.objects.filter(status__in=['approved', 'resolved']).order_by('-submitted_at')
    return render(request, 'myapp/personas.html', {'reports': reports})

@login_required(login_url='/login/')
def my_reports(request):
    reports = WaterFaultReport.objects.filter(user=request.user).order_by('-submitted_at')
    return render(request, 'myapp/my_reports.html', {'reports': reports})

# ADMIN DASHBOARD VIEWS
@login_required(login_url='/login/')
@user_passes_test(is_admin)
def admin_dashboard(request):
    pending_reports = WaterFaultReport.objects.filter(status='pending').order_by('-submitted_at')
    approved_reports = WaterFaultReport.objects.filter(status='approved').order_by('-submitted_at')
    resolved_reports = WaterFaultReport.objects.filter(status='resolved').order_by('-submitted_at')
    rejected_reports = WaterFaultReport.objects.filter(status='rejected').order_by('-submitted_at')
    
    stats = {
        'total': WaterFaultReport.objects.count(),
        'pending': pending_reports.count(),
        'approved': approved_reports.count(),
        'resolved': resolved_reports.count(),
        'rejected': rejected_reports.count(),
    }
    
    return render(request, 'myapp/admin_dashboard.html', {
        'pending_reports': pending_reports,
        'approved_reports': approved_reports,
        'resolved_reports': resolved_reports,
        'rejected_reports': rejected_reports,
        'stats': stats,
    })

@login_required(login_url='/login/')
@user_passes_test(is_admin)
def admin_update_report(request, report_id):
    report = get_object_or_404(WaterFaultReport, id=report_id)
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        admin_feedback = request.POST.get('admin_feedback', '')
        
        if new_status in ['pending', 'approved', 'resolved', 'rejected']:
            report.status = new_status
            report.admin_feedback = admin_feedback
            report.save()
            messages.success(request, f'Report #{report.id} updated to {report.get_status_display()}')
        
        return redirect('admin_dashboard')
    
    return render(request, 'myapp/admin_update_report.html', {'report': report})

@login_required(login_url='/login/')
@user_passes_test(is_admin)
def admin_delete_report(request, report_id):
    report = get_object_or_404(WaterFaultReport, id=report_id)
    
    if request.method == 'POST':
        report.delete()
        messages.success(request, f'Report #{report_id} has been deleted.')
        return redirect('admin_dashboard')
    
    return render(request, 'myapp/admin_confirm_delete.html', {'report': report})