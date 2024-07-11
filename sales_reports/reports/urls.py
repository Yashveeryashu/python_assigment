
# ----------------------------------------------------
from django.urls import path
from .views import manage_emails ,daily_report

urlpatterns = [
    path('manage-emails/', manage_emails, name='manage_emails'),
    path('daily-report/', daily_report, name='daily_report'),

]




# daily reports template dekani h to vo kese kre ge or ek word file ban k bhejni  h  