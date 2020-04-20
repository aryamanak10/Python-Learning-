import smtplib

username = 'akakad671@gmail.com'
password = 'aryamanisgr8@'

def send_mail(text='Email Body', subject='Hello World', from_email='akakad671@gmail.com', to_emails=None):
    assert isinstance(to_emails, list)

    # login in to my smtp server
    server = smtplib.SMTP(host='smtp.gmail.com', port = 547)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)
    server.quit()

    # with smtplib.SMTP() as server:
    #    server.login()
    #    pass 