import time
import os
import phonenumbers
import sqlalchemy
from models import orders, session

SLEEP_TIME = os.getenv("SLEEP_TIME", 180)


def normalise_phone_num(phone_num):
    return phonenumbers.parse(phone_num, "RU").national_number


def get_not_normal_phone_nums():
    return session.query(orders).filter(orders.normal_phones.is_(None)).all()


def main():
    while True:
        try:
            not_normal_phone_nums = get_not_normal_phone_nums()
            for contact in not_normal_phone_nums:
                contact.normal_phones = normalise_phone_num(contact.contact_phone)
            session.commit()
            time.sleep(SLEEP_TIME)
        except sqlalchemy.exc.DBAPIError:
            session.rollback()
            time.sleep(SLEEP_TIME)


if __name__ == '__main__':
    main()
