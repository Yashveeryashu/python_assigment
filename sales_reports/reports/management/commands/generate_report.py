# # reports/management/commands/generate_report.py
# from django.core.management.base import BaseCommand
# from django.core.mail import send_mail
# from reports.utils import process_excel
# from reports.models import ProcessedData, EmailAddress
# import os

# class Command(BaseCommand):
#     help = 'Generates and sends daily sales reports'

#     def handle(self, *args, **kwargs):
#         file_path = 'reports/attachments/Untitled spreadsheet.xlsx'
        
        
#         # Check if the file exists
#         if not os.path.exists(file_path):
#             self.stdout.write(self.style.ERROR(f"File not found: {file_path}"))
#             return
        
#         # Process Excel files
#         daily_total_sales, top_selling_product, total_sales_by_product = process_excel(file_path)
        
#         # Save to database
#         for _, row in daily_total_sales.iterrows():
#             ProcessedData.objects.create(
#                 store_id=row['Store Id'], 
#                 date=row['Date'], 
#                 daily_total_sales=row['Total Sales'], 
#                 top_selling_product=None, 
#                 total_sales_by_product=None
#             )
    

#         # Generate report
#         report = daily_total_sales.to_html() + top_selling_product.to_html() + total_sales_by_product.to_html()
        
#         # Get email addresses
#         emails = EmailAddress.objects.values_list('email', flat=True)
        
#         if not emails:
#             self.stdout.write(self.style.ERROR("No email addresses found in the database."))
#             return
        
#         # Send email
#         send_mail(
#             'Daily Sales Report',
#             'Here is the daily sales report.',
#             'Yashveerlangyan0@gmail.com',  # Replace with your sender email
#             list("Jatinlangyan@gmail.com","Yashveerlangyan@gmail.com"),
#             html_message=report,
#         )
        
#         self.stdout.write(self.style.SUCCESS("Daily sales report sent successfully."))

# reports/management/commands/generate_report.py
# from django.core.management.base import BaseCommand
# from django.core.mail import send_mail
# from reports.utils import process_excel
# from reports.models import RawData, ProcessedData, EmailAddress
# import os
# import pandas as pd

# class Command(BaseCommand):
#     help = 'Generates and sends daily sales reports'

#     def handle(self, *args, **kwargs):
#         # Process all Excel files in the attachments directory
#         attachment_dir = 'reports/attachments/'
#         all_files = [os.path.join(attachment_dir, f) for f in os.listdir(attachment_dir) if f.endswith('.xlsx')]
        
#         combined_data = pd.DataFrame()
#         for file in all_files:
#             daily_total_sales, top_selling_product, total_sales_by_product = process_excel(file)
#             combined_data = combined_data.append(daily_total_sales, ignore_index=True)

#         # Combine all data
#         combined_data = combined_data.groupby('store_id').sum().reset_index()

#         # Save to database
#         for _, row in combined_data.iterrows():
#             ProcessedData.objects.create(store_id=row['store_id'], date=row.get('date', None), daily_total_sales=row['total_sales'], top_selling_product=None, total_sales_by_product=None)

#         # Generate report
#         report = combined_data.to_html()

#         # Get email addresses
#         emails = EmailAddress.objects.values_list('email', flat=True)

#         # Send email
#         send_mail(
#             'Daily Sales Report',
#             'Here is the daily sales report.',
#             'Yashveerlangyan0@gmail.com',  # Replace with your sender email
#             list("Jatinlangyan@gmail.com","Yashveerlangyan@gmail.com"),
#             html_message=report,
#         )
#         self.stdout.write(self.style.SUCCESS("Daily sales report sent successfully."))


# reports/management/commands/generate_report.py
# from django.core.management.base import BaseCommand
# from django.core.mail import send_mail
# from reports.utils import process_excel
# from reports.models import RawData, ProcessedData, EmailAddress
# import os
# import pandas as pd

# class Command(BaseCommand):
#     help = 'Generates and sends daily sales reports'

#     def handle(self, *args, **kwargs):
#         # Process all Excel files in the attachments directory
#         attachment_dir = 'reports/attachments/'
#         all_files = [os.path.join(attachment_dir, f) for f in os.listdir(attachment_dir) if f.endswith('.xlsx')]
        
#         combined_data = pd.DataFrame()
#         for file in all_files:
#             daily_total_sales, top_selling_product, total_sales_by_product = process_excel(file)
#             combined_data = pd.concat([combined_data, daily_total_sales], ignore_index=True)

#         # Combine all data
#         combined_data = combined_data.groupby('store_id').sum().reset_index()

#         # Save to database
#         for _, row in combined_data.iterrows():
#             ProcessedData.objects.create(
#                 store_id=row['store_id'], 
#                 date=row.get('date', None), 
#                 daily_total_sales=row['total_sales'], 
#                 top_selling_product=None, 
#                 total_sales_by_product=None
#             )

#         # Generate report
#         report = combined_data.to_html()

#         # Get email addresses
#         emails = EmailAddress.objects.values_list('email', flat=True)

#         # Send email
#         send_mail(
#             'Daily Sales Report',
#             'Here is the daily sales report.',
#             'Yashveerlangyan0@gmail.com',  # Replace with your sender email
#             list("Yashveerlangyan@gmail.com"),
#             html_message=report,
            
#         )
#         self.stdout.write(self.style.SUCCESS("Daily sales report sent successfully."))

# reports/management/commands/generate_report.py
# from django.core.management.base import BaseCommand
# from django.core.mail import send_mail
# from reports.utils import process_excel
# from reports.models import ProcessedData, EmailAddress
# import os
# import pandas as pd

# class Command(BaseCommand):
#     help = 'Generates and sends daily sales reports'

#     def handle(self, *args, **kwargs):
#         # Process all Excel files in the attachments directory
#         attachment_dir = 'reports/attachments/'
#         all_files = [os.path.join(attachment_dir, f) for f in os.listdir(attachment_dir) if f.endswith('.xlsx')]
        
#         combined_data = pd.DataFrame()
#         for file in all_files:
#             daily_total_sales, top_selling_product, total_sales_by_product = process_excel(file)
#             combined_data = pd.concat([combined_data, daily_total_sales], ignore_index=True)

#         # Combine all data
#         combined_data = combined_data.groupby('store_id').sum().reset_index()

#         # Save to database
#         for _, row in combined_data.iterrows():
#             ProcessedData.objects.create(
#                 store_id=row['store_id'], 
#                 date=row.get('date', None), 
#                 daily_total_sales=row['total_sales'], 
#                 top_selling_product=None, 
#                 total_sales_by_product=None
#             )

#         # Generate report
#         report = combined_data.to_html()

#         # Get email addresses
#         emails = EmailAddress.objects.values_list('email', flat=True)

#         # Validate email addresses
#         valid_emails = []
#         for email in emails:
#             if '@' in email:
#                 valid_emails.append(email)
#             else:
#                 self.stdout.write(self.style.ERROR(f'Invalid email address found: {email}'))

#         # Send email if there are valid addresses
#         if valid_emails:
#             send_mail(
#                 'Daily Sales Report',
#                 'Here is the daily sales report.',
#                 'Yashveerlangyan0@gmail.com',
#                 list("Yashveerlangyan@gmail.com"),
#                 html_message=report,
#             )
#         else:
#             self.stdout.write(self.style.ERROR('No valid email addresses found.'))



# from django.core.management.base import BaseCommand
# from django.core.mail import send_mail
# from reports.utils import process_excel
# from reports.models import ProcessedData, EmailAddress
# import os
# import pandas as pd

# class Command(BaseCommand):
#     help = 'Generates and sends daily sales reports'

#     def handle(self, *args, **kwargs):
#         # Process all Excel files in the attachments directory
#         attachment_dir = 'reports/attachments/'
#         all_files = [os.path.join(attachment_dir, f) for f in os.listdir(attachment_dir) if f.endswith('.xlsx')]
        
#         combined_data = pd.DataFrame()
#         for file in all_files:
#             daily_total_sales, top_selling_product, total_sales_by_product = process_excel(file)
#             combined_data = pd.concat([combined_data, daily_total_sales], ignore_index=True)

#         # Combine all data
#         combined_data = combined_data.groupby('store_id').sum().reset_index()

#         # Save to database
#         for _, row in combined_data.iterrows():
#             ProcessedData.objects.create(
#                 store_id=row['store_id'], 
#                 date=row.get('date', None), 
#                 daily_total_sales=row['total_sales'], 
#                 top_selling_product=None, 
#                 total_sales_by_product=None
#             )

#         # Generate report
#         report = combined_data.to_html()

#         # Get email addresses
#         emails = EmailAddress.objects.values_list('email', flat=True)

#         # Validate email addresses
#         valid_emails = []
#         for email in emails:
#             if '@' in email:
#                 valid_emails.append(email)
#             else:
#                 self.stdout.write(self.style.ERROR(f'Invalid email address found: {email}'))

#         # Ensure we have valid emails before proceeding
#         if not valid_emails:
#             self.stdout.write(self.style.ERROR('No valid email addresses found.'))
#             return

#         # Send email if there are valid addresses
#         send_mail(
#             'Daily Sales Report',
#             'Here is the daily sales report.',
#             'Yashveerlangyan0@gmail.com',
#             valid_emails = [
#                "Jatinlangyan@gmail.com",
#                 "Yashveerlangyan@gmail.com",
               
#             ],  # Pass the list of valid email addresses here
#             html_message=report,
#         )
# from django.core.management.base import BaseCommand
# from django.core.mail import send_mail
# from reports.utils import process_excel
# from reports.models import ProcessedData, EmailAddress
# import os
# import pandas as pd

# class Command(BaseCommand):
#     help = 'Generates and sends daily sales reports'

#     def handle(self, *args, **kwargs):
#         # Process all Excel files in the attachments directory
#         attachment_dir = 'reports/attachments/'
#         all_files = [os.path.join(attachment_dir, f) for f in os.listdir(attachment_dir) if f.endswith('.xlsx')]
        
#         combined_data = pd.DataFrame()
#         for file in all_files:
#             daily_total_sales, top_selling_product, total_sales_by_product = process_excel(file)
#             combined_data = pd.concat([combined_data, daily_total_sales], ignore_index=True)

#         # Combine all data
#         combined_data = combined_data.groupby('store_id').sum().reset_index()

#         # Save to database
#         for _, row in combined_data.iterrows():
#             ProcessedData.objects.create(
#                 store_id=row['store_id'], 
#                 date=row.get('date', None), 
#                 daily_total_sales=row['total_sales'], 
#                 top_selling_product=None, 
#                 total_sales_by_product=None
#             )

#         # Generate report
#         report = combined_data.to_html()

#         # Get email addresses
#         emails = EmailAddress.objects.values_list('email', flat=True)

#         # Validate email addresses
#         valid_emails = []
#         for email in emails:
#             if '@' in email:
#                 valid_emails.append(email)
#             else:
#                 self.stdout.write(self.style.ERROR(f'Invalid email address found: {email}'))

#         # Ensure we have valid emails before proceeding
#         if not valid_emails:
#             self.stdout.write(self.style.ERROR('No valid email addresses found.'))
#             return

#         # Send email if there are valid addresses
#         send_mail(
#             'Daily Sales Report',
#             'Here is the daily sales report.',
#             'Yashveerlangyan0@gmail.com',
#             valid_emails,  # Use valid_emails list here
#             html_message=report,
#         )


# from django.core.management.base import BaseCommand
# from django.core.mail import send_mail
# from reports.utils import process_excel
# from reports.models import ProcessedData, EmailAddress
# import os
# import pandas as pd

# class Command(BaseCommand):
#     help = 'Generates and sends daily sales reports'

#     def handle(self, *args, **kwargs):
#         # Process all Excel files in the attachments directory
#         attachment_dir = 'reports/attachments/'
#         all_files = [os.path.join(attachment_dir, f) for f in os.listdir(attachment_dir) if f.endswith('.xlsx')]
        
#         combined_data = pd.DataFrame()
#         for file in all_files:
#             processed_data = process_excel(file)
#             combined_data = pd.concat([combined_data, processed_data], ignore_index=True)

#         # Combine all data
#         combined_data = combined_data.groupby(['Store ID', 'Date']).agg({
#             'Total Sales': 'sum',
#             'Top Selling Product': lambda x: x.mode()[0] if not x.mode().empty else 'None'
#         }).reset_index()

#         # Save to database
#         for _, row in combined_data.iterrows():
#             ProcessedData.objects.create(
#                 store_id=row['Store ID'], 
#                 date=row['Date'], 
#                 total_sales=row['Total Sales'], 
#                 top_selling_product=row['Top Selling Product']
#             )

#         # Generate report
#         report = combined_data.to_html()

#         # Get email addresses
#         emails = EmailAddress.objects.values_list('email', flat=True)

#         # Validate email addresses
#         valid_emails = []
#         for email in emails:
#             if '@' in email:
#                 valid_emails.append(email)
#             else:
#                 self.stdout.write(self.style.ERROR(f'Invalid email address found: {email}'))

#         # Ensure we have valid emails before proceeding
#         if not valid_emails:
#             self.stdout.write(self.style.ERROR('No valid email addresses found.'))
#             return

#         # Send email if there are valid addresses
#         send_mail(
#             'Daily Sales Report',
#             'Here is the daily sales report.',
#             'Yashveerlangyan0@gmail.com',
#             valid_emails,  # Use valid_emails list here
#             html_message=report,
#         )
from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from reports.utils import process_excel
from reports.models import ProcessedData, EmailAddress
import os
import pandas as pd

class Command(BaseCommand):
    help = 'Generates and sends daily sales reports'

    def handle(self, *args, **kwargs):
        # Process all Excel files in the attachments directory
        attachment_dir = 'reports/attachments/'
        all_files = [os.path.join(attachment_dir, f) for f in os.listdir(attachment_dir) if f.endswith('.xlsx')]
        
        combined_data = pd.DataFrame()
        for file in all_files:
            processed_data = process_excel(file)
            combined_data = pd.concat([combined_data, processed_data], ignore_index=True)

        # Combine all data
        combined_data = combined_data.groupby(['Store ID', 'Date']).agg({
            'Total Sales': 'sum',
            'Top Selling Product': lambda x: x.mode()[0] if not x.mode().empty else 'None'
        }).reset_index()

        # Save to database
        for _, row in combined_data.iterrows():
            ProcessedData.objects.create(
                store_id=row['Store ID'], 
                date=row['Date'], 
                total_sales=row['Total Sales'], 
                top_selling_product=row['Top Selling Product']
            )

        # Generate report
        report = combined_data.to_html()

        # Get email addresses
        emails = EmailAddress.objects.values_list('email', flat=True)

        # Validate email addresses
        valid_emails = []
        for email in emails:
            if '@' in email:
                valid_emails.append(email)
            else:
                self.stdout.write(self.style.ERROR(f'Invalid email address found: {email}'))

        # Ensure we have valid emails before proceeding
        if not valid_emails:
            self.stdout.write(self.style.ERROR('No valid email addresses found.'))
            return

        # Send email if there are valid addresses
        send_mail(
            'Daily Sales Report',
            'Here is the daily sales report.',
            'Yashveerlangyan0@gmail.com',
            valid_emails,  # Use valid_emails list here
            html_message=report,
        )
