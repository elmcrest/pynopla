"""
Simpe smtp class, for consistency should also be async (aiosmtp f.e.) but for now I'm fine with it 😜
"""

import smtplib
from smtplib import SMTPAuthenticationError
import asyncio
from email.mime.text import MIMEText


loop = asyncio.get_event_loop()


class MailSender:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password

    @classmethod
    async def create(cls, host, user, password):
        self = MailSender(host, user, password)
        try:
            server = smtplib.SMTP_SSL(host, 465)
            server.ehlo()
            server.login(user, password)
            server.close()
        except SMTPAuthenticationError:
            print(f"Can't connect to smtp server {host}")
            loop.stop()
        return self

    async def send_mail(self, recipient, message):
        msg = MIMEText(message)
        msg['subject'] = 'Status report from pynopla.'
        try:
            server = smtplib.SMTP_SSL(self.host, 465)
            server.ehlo()
            server.login(self.user, self.password)
            server.send_message(msg, self.user, recipient)
            server.close()
        except SMTPAuthenticationError:
            print(f"Can't connect to smtp server {self.host}")
