from datetime import datetime, date, timedelta
import random


SUPPORTED_STRING_DATE_FORMATS = {
    'DD.MM.YYYY': '%d.%m.%Y',
    'YYYY-MM-DD': '%Y-%m-%d',
    'DD/MM/YYYY': '%d/%m/%Y',
}


def get_birthdays_per_week(users: list[dict], datetime_from=None) -> None:
    """
    prints reminding notification with names of given
    users whose birthdays are in the following week
    For example:
        Friday: Ryan
        Monday: Andrew
        Wednesday: William
    Users whose birthdays was on Saturday and Sunday are printed on Monday
    :param users: list of dicts. Each dict represents user and has keys 'name' and 'birthday'
                'birthday' may be given as datetime or date or str object
    :param datetime_from: optional, takes current date if nothing was given
    :return: None
    """

    datetime_from = datetime_from or datetime.now()
    start_date = datetime_from.date()
    day_from = start_date.weekday()
    if day_from == 0:  # if day_from is Monday
        start_date -= timedelta(days=2)
    if day_from == 6:  # if day_from is Sunday
        start_date -= timedelta(days=1)

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    names_of_week = [[] for _ in range(7)]  # indices are days of week

    for user in users:
        user_name = user.get('name', 'unknown_user')
        user_birthday = user.get('birthday', None)

        user_birthday_date = handle_user_birthday(user_birthday)
        if not user_birthday_date:
            continue

        next_user_birthday = user_birthday_date.replace(year=start_date.year)
        if next_user_birthday < start_date:
            next_user_birthday = user_birthday_date.replace(year=start_date.year + 1)

        days_to_birthday = (next_user_birthday - start_date).days
        if days_to_birthday < 7:
            day = next_user_birthday.weekday()
            names_of_week[day].append(user_name)

    names_of_week[0] = names_of_week[5] + names_of_week[6] + names_of_week[0]
    day_from = 0 if day_from > 4 else day_from

    for i in range(day_from, day_from + 5):
        if names_of_week[i % 5]:
            print(f"{days[i % 5]}: {', '.join(names_of_week[i % 5])}")


def get_date_from_string(date_string: str) -> date | None:
    """
    makes and returns date object from given date_string
    according to SUPPORTED_STRING_DATE_FORMATS
    :param date_string: str
    :return: date object or None
    """
    for pattern in SUPPORTED_STRING_DATE_FORMATS.values():
        try:
            dt = datetime.strptime(date_string, pattern)
        except ValueError:
            continue
        else:
            return dt.date()


def handle_user_birthday(user_birthday) -> date | None:
    """
    makes and returns date object from given user_birthday
    :param user_birthday: may be given as datetime or date or str object
    :return: date object or None
    """
    if isinstance(user_birthday, datetime):
        return user_birthday.date()
    if isinstance(user_birthday, date):
        return user_birthday
    if isinstance(user_birthday, str):
        return get_date_from_string(user_birthday)
    else:
        return None


def main():
    users = [
        {"name": "John", "birthday": "1985-08-07"},
        {"name": "Emily", "birthday": "1992-08-06"},
        {"name": "Michael", "birthday": "1978-07-10"},
        {"name": "Sarah", "birthday": "1990-08-09"},
        {"name": "David", "birthday": "1987-09-30"},
        {"name": "Jessica", "birthday": "1983-02-28"},
        {"name": "Daniel", "birthday": "1995-08-10"},
        {"name": "Jennifer", "birthday": "1989-04-06"},
        {"name": "Christopher", "birthday": "1980-12-24"},
        {"name": "Elizabeth", "birthday": "1998-08-09"},
        {"name": "Matthew", "birthday": "1984-07-08"},
        {"name": "Olivia", "birthday": "1993-10-14"},
        {"name": "Andrew", "birthday": "1976-08-13"},
        {"name": "Sophia", "birthday": "1991-09-20"},
        {"name": "William", "birthday": "1982-08-16"},
        {"name": "Ava", "birthday": "1997-11-08"},
        {"name": "Ryan", "birthday": "1986-08-11"},
        {"name": "Natalie", "birthday": "1994-08-05"},
        {"name": "James", "birthday": "1981-07-15"},
        {"name": "Grace", "birthday": "1996-06-23"}
    ]
    my_date = datetime(2023, 1, 1)
    delta = timedelta(days=random.randint(0, 365))
    my_date += delta
    print(f'Result for {my_date.strftime("%A %d %B %Y")}: ')
    get_birthdays_per_week(users, my_date)


if __name__ == '__main__':
    main()
