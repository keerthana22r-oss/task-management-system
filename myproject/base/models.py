from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('critical', 'Critical'),
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('review', 'Review'),
        ('completed', 'Completed'),
    ]
    
    # Core Fields
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, blank=True)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    # Time Management
    estimated_hours = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    actual_hours = models.DecimalField(max_digits=5, decimal_places=1, default=0)
    due_date = models.DateField(null=True, blank=True)
    
    # Progress
    progress = models.IntegerField(default=0)
    
    # Relationships
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tasks')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='created_tasks')
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    # Soft delete
    is_deleted = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-priority', 'due_date']
        indexes = [
            models.Index(fields=['status', 'priority']),
            models.Index(fields=['assigned_to', 'status']),
        ]
    
    def save(self, *args, **kwargs):
        status_progress = {
            'pending': 0,
            'in_progress': 50,
            'review': 75,
            'completed': 100,
        }
        self.progress = status_progress.get(self.status, self.progress)
        
        if self.status == 'completed' and not self.completed_at:
            self.completed_at = timezone.now()
        elif self.status != 'completed':
            self.completed_at = None
            
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    @property
    def is_overdue(self):
        """Check if task is overdue"""
        if self.due_date and self.status != 'completed':
            return timezone.now().date() > self.due_date
        return False
    
    @property
    def is_due_soon(self):
        """Check if task is due within 2 days"""
        if self.due_date and self.status != 'completed':
            days_left = (self.due_date - timezone.now().date()).days
            return 0 <= days_left <= 2
        return False
    
    @property
    def days_remaining(self):
        """Get days remaining until due date"""
        if self.due_date and self.status != 'completed':
            days = (self.due_date - timezone.now().date()).days
            if days < 0:
                return f"{abs(days)} days overdue"
            elif days == 0:
                return "Due today"
            else:
                return f"{days} days remaining"
        return "No deadline"