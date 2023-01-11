# https://habr.com/ru/post/709676/
from PyEasyQiwi import QiwiConnection
from TOKEN import QIWI_TOKEN, QIWI_DESIGN_NAME

conn = QiwiConnection(QIWI_TOKEN)

value = 3010.11
currency = "RUB"
delay = 15
description = "test_user_ID"
theme_code = QIWI_DESIGN_NAME
comment = "Привет, Хабр!"
qiwi_pay = False
card_pay = True

pay_url, bill_id, response = conn.create_bill(value, currency, delay, description, theme_code, comment, qiwi_pay, card_pay)
print("Ссылка для оплаты: ", pay_url)

status, response = conn.check_bill(bill_id)
print(status)
# WAITING - счёт ожидает оплаты,
# PAID - счёт ожидает оплаты,
# REJECTED - счёт отклонён,
# EXPIRED - срок оплаты просрочен