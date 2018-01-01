import smtplib
import credentials
import settings
from html_builder import HtmlBuilder
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(subject, films, tv_shows):
    smtp_server = 'smtp.gmail.com'
    gmail_user = credentials.gmail_user
    gmail_pwd = credentials.gmail_pwd
    FROM = 'tiftesttif@gmail.com'
    TO = settings.recipients

    msg = MIMEMultipart('alternative')
    msg['To'] = ', '.join(TO)
    msg['From'] = FROM
    msg['Subject'] = subject

    text = "Unable to display HTML message"
    part1 = MIMEText(text, 'plain')

    html_builder = HtmlBuilder()

    html = html_builder.build_html(films, tv_shows)[0]
    part2 = MIMEText(html, 'html')

    msg.attach(part1)
    msg.attach(part2)

    try:
        s = smtplib.SMTP(smtp_server, 587)
        s.ehlo()
        s.starttls()
        s.login(gmail_user, gmail_pwd)
        s.sendmail(FROM, TO, msg.as_string())
        s.quit()
        print('successfully sent the mail')
    except smtplib.SMTPException as err:
        print("failed to send mail: " + str(err))
