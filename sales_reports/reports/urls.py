from django.urls import path
from .views import daily_summary, manage_emails

urlpatterns = [
    path('daily-summary/', daily_summary, name='daily_summary'),
    path('manage-emails/', manage_emails, name='manage_emails'),
]
