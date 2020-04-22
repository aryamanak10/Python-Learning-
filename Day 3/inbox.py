import imaplib
import email

host = 'imap.gmail.com'
username = 'akakad671@gmail.com'
password = 'aryamanisgr8@'

mail=imaplib.IMAP4_SSL(host)
mail.login(username, password)
mail.select("inbox")
_, search_data = mail.search(None, 'UNSEEN')

for num in search_data[0].split():
    #print(num)
    _, data = mail.fetch(num, '(RFC822)')
    #print(data[0])
    _, b = data[0]
    email_message = email.message_from_bytes(b)
    # print(email_message)
    for header in ['subject', 'to', 'from', 'date']:
        print("{}: {}".format(header, email_message[header]))
    for part in email_message.walk():
        if part.get_content_type == "text/plain" or part.get_content_type() == "text/html":
            body = part.get_payload(decode=True)
            print(body.decode())