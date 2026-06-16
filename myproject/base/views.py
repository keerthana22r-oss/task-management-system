
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils import timezone  # ← ADD THIS LINE
from django.http import JsonResponse
from datetime import date

@login_required
def home(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        task = form.save(commit=False)
        task.created_by = request.user
        task.save()
        messages.success(request, 'Task created successfully!')
        return redirect('read_task')
    return render(request, 'home.html', {'form': form})

@login_required
def read_task(request):
    # Base queryset - users only see their own tasks
    tasks = Task.objects.filter(created_by=request.user, is_deleted=False)
    
    # Search functionality
    search_query = request.GET.get('q', '')
    if search_query:
        tasks = tasks.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    # Advanced filtering
    priority_filter = request.GET.get('priority')
    if priority_filter:
        tasks = tasks.filter(priority=priority_filter)
    
    status_filter = request.GET.get('status')
    if status_filter:
        tasks = tasks.filter(status=status_filter)
    
    # Ordering
    sort_by = request.GET.get('sort', '-created_at')
    tasks = tasks.order_by(sort_by)
    
    # Get counts for dashboard stats
    context = {
        'tasks': tasks,
        'search': search_query,
        'priority_filter': priority_filter,
        'status_filter': status_filter,
        'total_tasks': tasks.count(),
        'completed_tasks': tasks.filter(status='completed').count(),
        'overdue_tasks': tasks.filter(due_date__lt=timezone.now().date()).exclude(status='completed').count(),
        'priority_choices': Task.PRIORITY_CHOICES,
        'status_choices': Task.STATUS_CHOICES,
    }
    return render(request, 'read_task.html', context)

@login_required
def update_task(request, pk):
    task = get_object_or_404(Task, id=pk, created_by=request.user, is_deleted=False)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        messages.success(request, 'Task updated successfully!')
        return redirect('read_task')
    return render(request, 'update_task.html', {'form': form, 'task': task})

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk, created_by=request.user)
    if request.method == 'POST':
        # Soft delete instead of permanent
        task.is_deleted = True
        task.save()
        messages.success(request, 'Task moved to trash!')
        return redirect('read_task')
    return render(request, 'delete_task.html', {'task': task})  # Pass task to template!


def check_task_alerts(request):
    """API endpoint to check for task alerts"""
    if not request.user.is_authenticated:
        return JsonResponse({'alerts': []})
    
    tasks = Task.objects.filter(created_by=request.user, is_deleted=False)
    alerts = []
    
    for task in tasks:
        if task.is_overdue:
            alerts.append({
                'type': 'overdue',
                'icon': '⚠️',
                'title': 'Task Overdue!',
                'message': f'"{task.title}" is overdue',
                'task_url': f'/base/update/{task.id}/'
            })
        elif task.is_due_soon:
            days_left = (task.due_date - date.today()).days
            alerts.append({
                'type': 'due-soon',
                'icon': '⏰',
                'title': 'Due Soon',
                'message': f'"{task.title}" is due in {days_left} days',
                'task_url': f'/base/update/{task.id}/'
            })
    
    return JsonResponse({'alerts': alerts[:5]})