import pymysql
import datetime
import re

def get_tg_id(tg_id, user_name):
    try:
        with pymysql.connect(host='localhost', port=3306, user="root", password="") as connection:
            with connection.cursor() as cursor:
                cursor.execute("""USE ssb""")
                cursor.execute(f"""SELECT tg_id FROM users WHERE {tg_id} = tg_id""")
                result = cursor.fetchone()

                if result is None:
                    current_time = datetime.datetime.now()
                    year = current_time.year
                    month = current_time.month
                    day = current_time.day
                    len_month = len(str(month))
                    len_day = len(str(day))
                    if len_month != 2 and len_day != 2:
                        print(f"{year}-0{month}-0{day}")
                        cursor.execute(
                            f"""INSERT INTO users (tg_id, date_start, user_name) VALUES ('{tg_id}, {year}-0{month}-0{day}', '{user_name}')""")
                        connection.commit()
                    elif len_day != 2 and len_month == 2:
                        print(f"{year}-{month}-0{day}")
                        cursor.execute(
                            f"""INSERT INTO users (tg_id, date_start, user_name) VALUES ({tg_id}, '{year}-{month}-0{day}', '{user_name}')""")
                        connection.commit()
                    elif len_day == 2 and len_month != 2:
                        print(f"{year}-0{month}-{day}")
                        cursor.execute(
                            f"""INSERT INTO users (tg_id, date_start, user_name) VALUES ({tg_id}, '{year}-0{month}-{day}', '{user_name}')""")
                        connection.commit()

    except pymysql.Error as e:
        pass

def get_money(tg_id):
    try:
        with pymysql.connect(host='localhost', port=3306, user="root", password="") as connection:
            with connection.cursor() as cursor:
                cursor.execute("""USE ssb""")
                cursor.execute(f"""SELECT money FROM users WHERE {tg_id} = tg_id""")
                result = cursor.fetchone()

                t_str = str(result)
                numbers = re.findall(r"'(.*?)'", t_str)

                return numbers
    except pymysql.Error as e:
        pass

def get_data(tg_id):
    try:
        with pymysql.connect(host='localhost', port=3306, user="root", password="") as connection:
            with connection.cursor() as cursor:
                cursor.execute("""USE ssb""")
                cursor.execute(f"""SELECT date_start FROM users WHERE {tg_id} = tg_id""")
                time = cursor.fetchone()

                return time
    except pymysql.Error as e:
        pass

def get_full_data(day, month):
    len_month = len(str(month))
    len_day = len(str(day))

    if len_month != 2 and len_day != 2:
        day = f"0{day}"
        month = f"0{month}"

    elif len_day != 2 and len_month == 2:
        day = f"0{day}"

    elif len_day == 2 and len_month != 2:
        month = f"0{month}"
    return f"{month}:{day}"
