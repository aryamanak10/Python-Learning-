def my_print(txt):
    print(txt)

msg_template  = """Hello {name},
Thank you for joining {website}.We are very
happy to have you with us.
"""

def format_msg(my_name="Aryaman",my_website="github.com"):
    my_msg = msg_template.format(name=my_name, website=my_website)
    # print(my_msg)
    return my_msg