
# from django.shortcuts import render,redirect
# from .models import ProcessedData
# from .form import EmailAddressForm
# from .models import EmailAddress 
# from django.core.mail import send_mail

# def daily_summary(request):
#     reports = ProcessedData.objects.all()
#     return render(request, 'reports/daily_report.html', {'reports': reports})




# def manage_emails(request):
#     if request.method == "POST":
#         form = EmailAddressForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('manage_emails')
#     else:
#         form = EmailAddressForm()

#     emails = EmailAddress.objects.all()
#     return render(request, 'reports/manage_emails.html', {'form': form, 'emails': emails})


# def homepage(request):
#     send_mail (
#         'testing is mail',
#         'here is the message',
#         'Yashveerlangyan0@gmail.com',
#         ['Yashveerlangyan@gmail.com'],
#         fail_silently=False,
#     )



# --------------------------------------------------------------------------------
# reports/views.py
from django.shortcuts import render, redirect
from .models import EmailAddress,ProcessedData
from .forms import EmailForm

def manage_emails(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_emails')
    else:
        form = EmailForm()
    emails = EmailAddress.objects.all()
    return render(request, 'reports/manage_emails.html', {'form': form, 'emails': emails})

# def report(request):
#     data1=ProcessedData.objects.all()

#     return render(request,"reports/daily_report.html",{"reports",data1})

def daily_report(request):
    reports = ProcessedData.objects.all()  # Fetch all processed data from the database
    return render(request, 'reports/daily_report.html', {'reports': reports})