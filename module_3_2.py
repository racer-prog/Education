
domain = ['.ru','.com','.net']


def send_email(message, recipient, sender = "university.help@gmail.com"):
    #print(f"{sender}:sender")
    #print(f"{recipient}: recipient")
    if "@" in str(recipient) and str(sender):
        a = str(sender)[-4:]
        b = str(recipient)[-4:]
        sen = ''
        rec = ''
        for i in domain:
            if i in a:
                #print(i, a)
                sen = "ok"
            if i in b:
                #print(i, b)
                rec = "ok"

        if sen == "ok" and rec == "ok":
            if recipient == sender:
                print("Нельзя отправить письмо самому себе!")
                return
            if sender == 'university.help@gmail.com':
                print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
                return
            if sender != 'university.help@gmail.com':
                print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
                return
        else:
            print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")


#print('1:')
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
#print('2:')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
#print('3:')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
#print('4:')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')