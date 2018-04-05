import os
import asyncio
from pynopla.client import InoplaClient
from pynopla.sendmail import MailSender
from pynopla.periodic import Periodic
from time import strftime, localtime

INOPLA_API_ID = os.environ.get('INOPLA_API_ID')
INOPLA_API_KEY = os.environ.get('INOPLA_API_KEY')
SMTP_HOST = os.environ.get('SMTP_HOST')
SMTP_USER = os.environ.get('SMTP_USER')
SMTP_PASS = os.environ.get('SMTP_PASS')
SMTP_RECIPIENT = os.environ.get('SMTP_RECIPIENT', SMTP_USER)
PERIODIC_TIME = int(os.environ.get('PERIODIC_TIME', 900))


async def check_and_report_online_users(client_object, smtp):
    await client_object.get_users()

    message = ''
    for user in client_object.users:
        user = client_object.users[user]
        if user.connected:
            continue
        else:
            message += f'User {user.name} is offline ({strftime("%c",localtime())}).\n'

    await smtp.send_mail(SMTP_RECIPIENT, message)


async def check_periodic(func, client_object, smpt):
    p = Periodic(lambda: func(client_object, smpt), PERIODIC_TIME)
    await p.start()


async def main():
    client_object = await InoplaClient.create(api_id=INOPLA_API_ID, api_key=INOPLA_API_KEY)
    smtp = await MailSender.create(SMTP_HOST, SMTP_USER, SMTP_PASS)
    loop.create_task(
        check_periodic(
            check_and_report_online_users, client_object, smtp
        )
    )

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
