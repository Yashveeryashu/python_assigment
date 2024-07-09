
from django.shortcuts import render,redirect
from .models import ProcessedData
from .form import EmailAddressForm
from .models import EmailAddress 


def daily_summary(request):
    reports = ProcessedData.objects.all()
    return render(request, 'reports/daily_report.html', {'reports': reports})




def manage_emails(request):
    if request.method == "POST":
        form = EmailAddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_emails')
    else:
        form = EmailAddressForm()

    emails = EmailAddress.objects.all()
    return render(request, 'reports/manage_emails.html', {'form': form, 'emails': emails})
