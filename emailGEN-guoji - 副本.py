import random
import string
print("======================================================")
print("=======================Hu=============================")
print("=======================欢=============================")
print("=======================迎=============================")
print("=======================你=============================")
print("======================================================")
print("======================================================")
#选择网站
Select_Web = int(input('选择网站1:ThaiTicketMajor,2:MELON,3:Interpark,4:Yes24 : '))
email = input("输入域名: ")
emails = [email]
if Select_Web == 1:
    email_number = int(input('需要生产的邮箱数:'))
    all_characters = string.ascii_letters + string.digits
    for _ in range(email_number):
                username_length = random.randint(6, 12)
                username = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(username_length))
                domain = random.choice(emails)
                email = username + '@' + domain
                password_length = random.randint(8, 16)
                password = ''.join(random.choice(all_characters) for _ in range(password_length))
                print(f"{email}:{password}\n")
elif Select_Web == 2 or Select_Web == 3:
    imap_gmail = input("输入imap_gmail: ")
    imap_gmail_password = input("输入imap_gmail_password: ")
    email_number = int(input('需要生产的邮箱数:'))
    Last_name = input('姓氏:')
    First_name = input('名字:')
    all_characters = string.ascii_letters + string.digits
    for _ in range(email_number):
                username_length = random.randint(6, 12)
                username = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(username_length))
                domain = random.choice(emails)
                email = username + '@' + domain
                password_length = random.randint(8, 16)
                password = ''.join(random.choice(all_characters) for _ in range(password_length))
                print(f"{email}:{password}:{imap_gmail}:{imap_gmail_password}:{Last_name}:{First_name}\n")
elif Select_Web == 4:
    imap_gmail = input("输入imap_gmail: ")
    imap_gmail_password = input("输入imap_gmail_password: ")
    email_number = int(input('需要生产的邮箱数:'))
    Last_name = input('姓氏:')
    First_name = input('名字:')
    user_Birthday = input('生日:like 19990504: ')
    all_characters = string.ascii_letters + string.digits
    for _ in range(email_number):
        username_length = random.randint(6, 12)
        username = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(username_length))
        domain = random.choice(emails)
        email = username + '@' + domain
        password_length = random.randint(8, 16)
        password = ''.join(random.choice(all_characters) for _ in range(password_length))
        print(f"{email}:{password}:{imap_gmail}:{imap_gmail_password}:{Last_name}:{First_name}:{user_Birthday}\n")


# 修改这里的数字可以改变生成的数量

