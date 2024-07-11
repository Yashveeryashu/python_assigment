# reports/management/commands/fetch_emails.py
import imaplib
import email
from email.header import decode_header
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Fetches emails with sales reports'

    def handle(self, *args, **kwargs):
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login('Yashveerlangyan0@gmail.com', 'awtd wfkt dwlo xmqz')
        mail.select('inbox')
        status, messages = mail.search(None, '(SUBJECT "Daily Sales Report")')
        messages = messages[0].split()
        for mail_id in messages:
            status, msg_data = mail.fetch(mail_id, '(RFC822)')
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    for part in msg.walk():
                        if part.get_content_maintype() == 'multipart':
                            continue
                        if part.get('Content-Disposition') is None:
                            continue
                        if 'attachment' in part.get('Content-Disposition'):
                            filename = part.get_filename()
                            if filename:
                                with open(f'reports/attachments/{filename}', 'wb') as f:
                                    f.write(part.get_payload(decode=True))
        mail.logout()
