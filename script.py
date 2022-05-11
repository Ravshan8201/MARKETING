import time
import schedule
from func import *

def send_message(context):


    connect = sqlite3.connect('users.sqlite')
    cur = connect.cursor()
    current_dt = datetime.now().strftime("%d.%m.%Y %H:%M")
    c_date, c_time = current_dt.split()
    date = cur.execute(select_MAINDATA.format(adct[0])).fetchall()
    time = cur.execute(select_MAINTIME.format(adct[0])).fetchall()
    f_ru = cur.execute(select_RU.format(adct[0])).fetchall()
    f_uz = cur.execute(select_UZ.format(adct[0])).fetchall()
    all_users = cur.execute(""" SELECT TG_ID  FROM Book WHERE BOOKDATA = "{}" AND TG_ID !=0 """.format(date)).fetchall()
    connect.commit()
    try:
        # Main
        date = date[0][0]
        time = time[0][0]
        f_ru = f_ru[0][0]
        f_uz = f_uz[0][0]
        all_users= all_users[0]
    except Exception:
        pass
    for e in all_users:
        s = cur.execute("""SELECT Stage FROM Users WHERE TG_ID= "{}" """.format(e))
        l = cur.execute("""SELECT Lang FROM Users WHERE TG_ID= "{}" """.format(e))
        if s== 6 and date ==c_date:
            context.bot.send_message(chat_id=e, text=dct[l][16])
            schedule.every().day.at("17:36").do(send_message())
            schedule.every().day.at("17:37").do(send_message())
while True:
    schedule.run_pending()
    time.sleep(1)