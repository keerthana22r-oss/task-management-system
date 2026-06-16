// static/js/notification.js
// Task Alert System

class TaskAlert {
    constructor() {
        this.alerts = [];
        this.init();
    }

    init() {
        this.checkDueDates();
        this.startAutoRefresh();
    }

    checkDueDates() {
        fetch('/base/check-alerts/')
            .then(response => response.json())
            .then(data => {
                if (data.alerts && data.alerts.length > 0) {
                    this.showAlerts(data.alerts);
                    this.updateBellIcon(data.alerts.length);
                }
            })
            .catch(error => console.log('No alerts'));
    }

    showAlerts(alerts) {
        alerts.forEach(alert => {
            this.displayToast(alert);
        });
    }

    displayToast(alert) {
        // Remove existing similar toast to prevent duplicates
        const existingToasts = document.querySelectorAll('.task-toast');
        existingToasts.forEach(toast => {
            if (toast.innerHTML.includes(alert.message)) {
                return;
            }
        });

        const toast = document.createElement('div');
        toast.className = `task-toast task-toast-${alert.type}`;
        toast.innerHTML = `
            <div class="toast-icon">${alert.icon}</div>
            <div class="toast-content">
                <div class="toast-title">${alert.title}</div>
                <div class="toast-message">${alert.message}</div>
                ${alert.task_url ? `<a href="${alert.task_url}" class="toast-action">View Task →</a>` : ''}
            </div>
            <button class="toast-close">&times;</button>
        `;
        
        document.body.appendChild(toast);
        
        const closeBtn = toast.querySelector('.toast-close');
        closeBtn.onclick = () => toast.remove();
        
        setTimeout(() => {
            if (toast.parentNode) toast.remove();
        }, 8000);
    }

    updateBellIcon(count) {
        const alertCount = document.getElementById('alertCount');
        if (alertCount) {
            if (count > 0) {
                alertCount.textContent = count;
                alertCount.style.display = 'inline-block';
            } else {
                alertCount.style.display = 'none';
            }
        }
    }

    startAutoRefresh() {
        setInterval(() => this.checkDueDates(), 300000);
    }
}

// Initialize when page loads
document.addEventListener('DOMContentLoaded', () => {
    window.taskAlert = new TaskAlert();
});