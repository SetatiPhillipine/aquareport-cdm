from django.shortcuts import render, redirect
from django.contrib import messages
from myapp.models import WaterFaultReport

def all_reports(request):
    reports = WaterFaultReport.objects.all().order_by('-submitted_at')
    return render(request, 'tracker/reports.html', {'reports': reports})

def stats(request):
    total = WaterFaultReport.objects.count()
    pending = WaterFaultReport.objects.filter(status='pending').count()
    in_progress = WaterFaultReport.objects.filter(status='approved').count()
    resolved = WaterFaultReport.objects.filter(status='resolved').count()
    reports = WaterFaultReport.objects.all().order_by('-submitted_at')
    
    return render(request, 'tracker/stats.html', {
        'total': total,
        'pending': pending,
        'in_progress': in_progress,
        'resolved': resolved,
        'reports': reports,
    })

def update_reports(request):
    if request.method == 'POST':
        # Check if we're saving a report
        if 'save_report' in request.POST:
            report_id = request.POST.get('save_report')
            report = WaterFaultReport.objects.get(id=report_id)
            
            new_status = request.POST.get(f'status_{report_id}')
            new_feedback = request.POST.get(f'feedback_{report_id}', '')
            
            if new_status:
                report.status = new_status
            report.admin_feedback = new_feedback
            report.save()
            
            messages.success(request, f'Report #{report_id} updated to {report.get_status_display()}')
        
        # Check if we're deleting a report
        elif 'delete_report' in request.POST:
            report_id = request.POST.get('delete_report')
            report = WaterFaultReport.objects.get(id=report_id)
            report.delete()
            messages.success(request, f'Report #{report_id} has been deleted')
        
        return redirect('stats')
    
    return redirect('stats')