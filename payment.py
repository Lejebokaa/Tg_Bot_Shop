import yookassa
from yookassa import Payment

from config import config


def create():
    yookassa.Configuration.account_id = config.YOOKASSA_ID
    yookassa.Configuration.secret_key = config.YOOKASSA_KEY

    payment = yookassa.Payment.create({
        "amount": {
            'value': 100 * 100,
            'currency': "RUB"
        },
        'paymnet_method_data': {
            'type': 'bank_card'
        },
        'confirmation': {
            'type': 'redirect',
            'return_url': 'https://t.me/SSB_yo_bot'
        },
        'description': f'Пополнение баланса на {100} Рублей',
        'capture': True
    })

    url = payment.confirmation.confirmation_url

    return url, payment.id

def oplata_check(id):
    payment = yookassa.Payment.find_one(id)
    if payment.status == 'succeeded':
        return True
    else:
        return False
