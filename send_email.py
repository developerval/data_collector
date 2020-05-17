from email.mime.text import MIMEText
import smtplib


def send_email(email, height, average, count):
    from_email = ENTER_YOUR_EMAIL_HERE
    from_pass = ENTER_YOUR_PASSWORD_HERE
    to_email = email

    subject = 'Height Data'

    message = f'Hi there, your height is <strong>{height}cm</strong> and the average height of all participants is <strong>{average}cm</strong>, this is calculated from <strong>{count}</strong> participants'

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_pass)
    gmail.send_message(msg)
