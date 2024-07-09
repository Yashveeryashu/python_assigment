import imaplib
import email
from email.header import decode_header

def read_emails():
    # Connect to the server
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    
    # Login to the account
    imap.login("Yashveerlangyan0@gmail.com", "yashuvishu@123")
    
    # Select the mailbox
    imap.select("inbox")
    
    # Search for emails with the subject "Daily Sales Report"
    status, messages = imap.search(None, 'SUBJECT "Daily Sales Report"')
    
    # Convert messages to a list of email IDs
    email_ids = messages[0].split()
    
    for email_id in email_ids:
        # Fetch the email by ID
        status, msg_data = imap.fetch(email_id, "(RFC822)")
        
        # Parse the email content
        msg = email.message_from_bytes(msg_data[0][1])
        for part in msg.walk():
            # Check for attachment
            if part.get_content_maintype() == "multipart":
                continue
            if part.get("Content-Disposition") is None:
                continue
            
            filename = part.get_filename()
            if filename:
                with open(f"downloads/{filename}", "wb") as f:
                    f.write(part.get_payload(decode=True))
    
    # Close the connection and logout
    imap.close()
    imap.logout()



import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.template.loader import render_to_string
from .models import EmailAddress, ProcessedData

def send_email(subject, body, to_emails):
    from_email = "Yashveerlangyan0@gmail.com"
    from_password = "yashuvishu@123"
    
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'html'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, from_password)
    server.sendmail(from_email, to_emails, msg.as_string())
    server.quit()

def send_daily_summary():
    emails = EmailAddress.objects.values_list('email', flat=True)
    body = render_to_string('reports/daily_summary.html', {'reports': ProcessedData.objects.all()})
    send_email("Daily Summary Report", body, emails)


