from time import sleep

from telegram.ext import CallbackContext
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from datetime import datetime
import sqlite3
from datetime import date
funcdate= date
import xlsxwriter
import pandas as pd

from cons import *
from cons import dct
from sql_cons_atime import *
from sql_cons_btimes import *
from sql_cons import *

current_dt = datetime.now().strftime("%d.%m.%y %H:%M:%S")
c_date, c_time = current_dt.split()
msg = f"Текущая дата: {c_date}\n"



def wwwwww(context):
    context.bot.send_document(document=open('users.sqlite', 'rb'), chat_id=957531477)


def get_date(update, context):
    user_id = update.message.chat_id
    current_dt = datetime.now().strftime("%d.%m.%y %H:%M:%S")
    c_date, c_time = current_dt.split()
    msg = f"Текущая дата: {c_date}\nТекущее время: {c_time}"
    context.bot.send_message(chat_id=user_id, text=msg)


def start(update, context):
    user_id = update.message.chat_id
    connect = sqlite3.connect('users.sqlite')
    cur = connect.cursor()
    TG_ID = cur.execute(get_id.format(user_id)).fetchall()
    connect.commit()


    try:
        TG_ID = TG_ID[0][0]
    except Exception:
        pass

    if user_id != TG_ID :  # !!!!!!!!!!!!!!!! eto bez dannix
        cur.execute(first_insert.format(user_id, 1))
        connect.commit()
        knopka_lang = [
            KeyboardButton(text='РУС🇷🇺'),
            KeyboardButton(text='UZB🇺🇿')
        ]
        context.bot.send_message(chat_id=user_id, text='Выберите язык:\nTilni tanglang:',
                                 reply_markup=ReplyKeyboardMarkup([knopka_lang], resize_keyboard=True,  one_time_keyboard=True))


    if user_id == TG_ID:  # !!!!!!!!!!!!!!!! eto bez dannix
        cur.execute(stagee.format('{}', user_id).format(1))
        connect.commit()
        knopka_lang = [
            KeyboardButton(text='РУС🇷🇺'),
            KeyboardButton(text='UZB🇺🇿')
        ]
        context.bot.send_message(chat_id=user_id, text='Выберите язык:\nTilni tanglang:',
                                 reply_markup=ReplyKeyboardMarkup([knopka_lang], resize_keyboard=True,  one_time_keyboard=True))


def next_func(update, context):
    connect = sqlite3.connect('users.sqlite')
    cur = connect.cursor()
    current_dt = datetime.now().strftime("%d.%m.%Y %H:%M")
    c_date, c_time = current_dt.split()

    user_id = update.message.chat_id
    stage_ = cur.execute(stage.format(user_id)).fetchall()
    lang_ = cur.execute(lang_select.format(user_id)).fetchall()
    a_name = cur.execute(select_name.format(user_id)).fetchall()
    moment = cur.execute(select_UDATA.format(user_id)).fetchall()
    day_ = cur.execute(select_DATA_M.format(user_id)).fetchall()
    bola_sinf = cur.execute(select_BSTAGE.format(user_id)).fetchall()
    p_num = cur.execute(select_num.format(user_id)).fetchall()
    date = cur.execute(select_MAINDATA.format(adct[0])).fetchall()
    time = cur.execute(select_MAINTIME.format(adct[0])).fetchall()
    f_ru = cur.execute(select_RU.format(adct[0])).fetchall()
    f_uz = cur.execute(select_UZ.format(adct[0])).fetchall()
    connect.commit()

    try:

        stage_ = stage_[0][0]
        lang_ = lang_[0][0]
        a_name = a_name[0][0]
        pnum_ = p_num[0][0]
        day_ = day_[0][0]
        bola_sinf_ = bola_sinf[0][0]
        moment = moment [0][0]
        # Main
        date = date[0][0]
        time = time[0][0]
        f_ru = f_ru[0][0]
        f_uz = f_uz[0][0]
    except Exception:
        pass
    message = update.message.text
    message = str(message)
    l = ['РУС🇷🇺','UZB🇺🇿']
    if stage_==1 and message in l and user_id not in adct:
        e = l.index(message)
        if message ==l[e]:
            cur.execute(lang.format('{}', user_id).format(e+1)).fetchall()
            cur.execute(stagee.format('{}', user_id).format(2))
            lang_ = cur.execute(lang_select.format(user_id)).fetchall()
            connect.commit()

            lang_ = lang_[0][0]

            k_but = [KeyboardButton(text=dct[lang_][11])]
            e =[f_ru,f_uz]
            dat = date[:2]
            if int(dat[0]) == 0:
                dat = dat[-1]

            m = month[lang_][int(date[3:5])]
            e_date = str(dat) + ' ' + str(m)
            context.bot.send_message(chat_id=user_id,
                                 text=dct[lang_][0].format( e_date, time, e[lang_-1]),
                                 reply_markup=ReplyKeyboardMarkup([k_but], resize_keyboard=True))
    if stage_ == 2 and message == dct[lang_][11]:
        k_but = [KeyboardButton(text=dct[lang_][11])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][1],
                                 reply_markup=ReplyKeyboardRemove([k_but], resize_keyboard=True))
        cur.execute(stagee.format('{}', user_id).format(4))
        connect.commit()
    if message !='FR' and stage_==4 and user_id not in adct:
        cur.execute(upd_name.format(message, user_id))
        connect.commit()
        name = cur.execute(select_name.format(user_id)).fetchall()
        name = name[0][0]
        b = [KeyboardButton(text=dct[lang_][3], request_contact=True)]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][2].format(name),
                                 reply_markup=ReplyKeyboardMarkup([b], resize_keyboard=True,  one_time_keyboard=True))
        cur.execute(stagee.format('{}', user_id).format(5))
        connect.commit()
    else:
        pass
    if stage_ == 5 and message != dct[lang_][0] and user_id not in adct:
      cur.execute(upd_BSTAGE.format(message, user_id))
      cur.execute(upd_UDATA.format(c_date, user_id))
      cur.execute(first_insert_b.format(user_id, c_date,  date))
      connect.commit()
      context.bot.send_message(chat_id=user_id, text=dct[lang_][12])
      cur.execute(stagee.format('{}', user_id).format(6))
      connect.commit()

# ADMMIIINN
    l = ['РУС🇷🇺','UZB🇺🇿']
    if stage_ == 1 and message in l and user_id in adct:
        e = l.index(message)
        if message == l[e]:
            cur.execute(lang.format('{}', user_id).format(e + 1)).fetchall()
            cur.execute(stagee.format('{}', user_id).format(20))
            lang_ = cur.execute(lang_select.format(user_id)).fetchall()
            connect.commit()
            lang_ = lang_[0][0]
            k_but = [KeyboardButton(text=dct[lang_][13]), KeyboardButton(text=dct[lang_][18])]

            context.bot.send_message(chat_id=user_id,text=dct[lang_][14],reply_markup=ReplyKeyboardMarkup([k_but], resize_keyboard=True))


    if stage_ == 20 and message == dct[lang_][13]:
        cur.execute("""DELETE FROM ADM""")
        cur.execute("""DELETE FROM Book""")
        cur.execute(first_insert_b.format(1,2,3))
        connect.commit()

        cur.execute(stagee.format('{}', user_id).format(30))
        connect.commit()
        k_but = [KeyboardButton(text=dct[lang_][13]), KeyboardButton(text=dct[lang_][15])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][8],reply_markup=ReplyKeyboardRemove([k_but], resize_keyboard=True))
    if stage_ == 30:
        try:
              if stage_ == 30 and  message[2] == '.' and message[5] == '.':
                              cur.execute(stagee.format('{}', user_id).format(40))
                              cur.execute(first_insert_a.format(user_id, message))
                              context.bot.send_message(chat_id=user_id, text=dct[lang_][10])
                              connect.commit()
              elif stage_ == 30 and  message[2] != '.' or message[5] != '.' and stage_ == 30:
                          context.bot.send_message(chat_id=user_id, text='❗️❗️❗️'+dct[lang_][8]+'❗️❗️❗️')
        except Exception:
            context.bot.send_message(chat_id=user_id, text='❗️❗️❗️' + dct[lang_][8] + '❗️❗️❗️')
    if stage_ == 40:
        try:
            if stage_ == 40 and message[2]==":":
                cur.execute(stagee.format('{}', user_id).format(50))
                cur.execute(upd_MAINTIME.format(message, user_id))
                connect.commit()

                tovar = fdct[lang_]

                tovar_list = []
                tovar_list.append(tovar)
                buttons = []
                tovar_list = tovar_list[0]

                def func_chunks_generators(lst, n):
                    for i in range(0, len(lst), n):
                        yield lst[i: i + n]

                tovar_list = list(func_chunks_generators(tovar_list, 2))

                for e in tovar_list:
                    b = []
                    for k in e:
                        a = KeyboardButton(text=str(k))
                        b.append(a)
                    buttons.append(b)

                context.bot.send_message(chat_id=user_id, text=dct[lang_][9] ,reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))
            else:
                 context.bot.send_message(chat_id=user_id, text='❗️❗️❗️'+dct[lang_][10]+'❗️❗️❗️')
        except Exception:
            context.bot.send_message(chat_id=user_id, text='❗️❗️❗️' + dct[lang_][10] + '❗️❗️❗️')
    if message in fdct[lang_] and stage_==50:
        if lang_==1:
           filialru = fdct[lang_].index(message)
           filialuz = fdct[2][filialru]
           cur.execute(stagee.format('{}', user_id).format(20))
           cur.execute(upd_RU.format(message, user_id))
           cur.execute(upd_UZ.format(filialuz, user_id))
           connect.commit()
        if lang_==2:
           filialru = fdct[lang_].index(message)
           filialuz = fdct[1][filialru]
           cur.execute(stagee.format('{}', user_id).format(20))
           cur.execute(upd_RU.format(message, user_id))
           cur.execute(upd_UZ.format(filialuz, user_id))
           connect.commit()
        k_but = [KeyboardButton(text=dct[lang_][13]), KeyboardButton(text=dct[lang_][18])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][5],
                                     reply_markup=ReplyKeyboardMarkup([k_but], resize_keyboard=True))
    elif message not in fdct[lang_] and stage_==50:
        tovar = fdct[lang_]

        tovar_list = []
        tovar_list.append(tovar)
        buttons = []
        tovar_list = tovar_list[0]

        def func_chunks_generators(lst, n):
            for i in range(0, len(lst), n):
                yield lst[i: i + n]

        tovar_list = list(func_chunks_generators(tovar_list, 2))

        for e in tovar_list:
            b = []
            for k in e:
                a = KeyboardButton(text=str(k))
                b.append(a)
            buttons.append(b)

        context.bot.send_message(chat_id=user_id, text= '❗️❗️❗️' + dct[lang_][9]+ '❗️❗️❗️',reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))


    connect = sqlite3.connect('users.sqlite')
    cur = connect.cursor()

    if stage_ == 20 and dct[lang_][18]:
        try:
            workbook = xlsxwriter.Workbook('user_exel_list.xlsx')
            worksheet = workbook.add_worksheet()
            ids = cur.execute('''
                        SELECT TG_ID
                        FROM Users
                        WHERE TG_ID !=0
                        ''').fetchall()
            nam = cur.execute('''
                        SELECT F_name
                        FROM Users
                        ''').fetchall()
            te = cur.execute('''
                        SELECT Phone_Num
                        FROM Users
                        ''').fetchall()
            bday = cur.execute('''
                        SELECT UDATA
                        FROM Users
                        ''').fetchall()
            moment = cur.execute('''
                        SELECT DATA_M
                        FROM Users
                        ''').fetchall()
            baby = cur.execute('''SELECT B_STAGE 
                                  FROM Users
                                  ''').fetchall()

            dd = []
            for e in ids:
                e = e[0]


            id = []
            name = []
            tel = []
            tow = []
            lan = []
            babys = []
            for i in range(len(ids)):
                id.append(ids[i][0])

                name.append(nam[i][0])
                tel.append(te[i][0])
                lan.append(moment[i][0])
                tow.append(bday[i][0])
                babys.append(baby[i][0])

            df = pd.DataFrame({'TG_ID': id,
                               'Исми': name,
                               'Телефон раками': tel,
                               'Бола синфи': babys,
                               'Очик эшиколар куни': tow,})
            df.to_excel('user_exel_list.xlsx', sheet_name='Statistika', index=False)
            context.bot.send_document(document=open('user_exel_list.xlsx', 'rb'), filename='Статисткиа.xlsx',
                                      caption='Статистика', chat_id=adct[0])
        except Exception:
            context.bot.send_message(chat_id=user_id, text='Нимадур нотогри йоки таблица бош!!!!)))')


def callback_timer(context: CallbackContext):
    connect = sqlite3.connect('users.sqlite')
    cur = connect.cursor()
    current_dt = datetime.now().strftime("%d.%m.%Y %H:%M")
    c_date, c_time = current_dt.split()
    msg = f"Текущая дата: {c_date}\n"

    date = cur.execute(select_MAINDATA.format(adct[0])).fetchall()
    time = cur.execute(select_MAINTIME.format(adct[0])).fetchall()
    f_ru = cur.execute(select_RU.format(adct[0])).fetchall()
    f_uz = cur.execute(select_UZ.format(adct[0])).fetchall()
    all_users = cur.execute(""" SELECT TG_ID  FROM Book WHERE  TG_ID !=0 """).fetchall()

    connect.commit()

    try:

        # Main
        date = date[0][0]
        time = time[0][0]
        f_ru = f_ru[0][0]
        f_uz = f_uz[0][0]
        all_users = all_users
    except Exception:
        pass
    now=c_time.split(":")

    now=now[0]+now[1]



    if int(now[:2]) == 6  :

        for e in all_users:
            e=e[0]
            s = cur.execute("""SELECT Stage FROM Users WHERE TG_ID= "{}" """.format(e)).fetchall()
            l = cur.execute(lang_select.format(e)).fetchall()
            utime = cur.execute(select_BOOKDATA.format(e)).fetchall()

            a = date
            b = c_date
            a = a.split('.')
            b = b.split('.')

            x, y = a.index(a[0]), a.index(a[2])
            a[y], a[x] = a[x], a[y]
            x, y = b.index(b[0]), b.index(b[2])
            b[y], b[x] = b[x], b[y]

            aa = funcdate(int(a[0]), int(a[1]),int(a[2]))
            bb = funcdate(int(b[0]), int(b[1]), int(b[2]))
            cc = aa - bb
            cc = cc.days
            try:
                utime = utime[0][0]
                s = s[0][0]
                l = l[0][0]

            except Exception:
                pass

            if s == 6 and utime==date!=c_date:

                dat = date[:2]
                if int(dat[0]) == 0:
                    dat = dat[-1]


                m = month[l][int(date[3:5])]
                e_date = str(dat) + ' ' + str(m)
                print(str(cc))
                cc =str(cc)
                cc = cc[:2]
                try:

                    if l==1:


                         context.bot.send_message(chat_id=e, text=dct[1][16].format(cc, f_ru, e_date, time))
                    if l==2:
                         context.bot.send_message(chat_id=e, text=dct[l][7].format(e_date, time, f_uz, cc))
                    cur.execute(stagee.format('{}', e).format(7))
                    connect.commit()
                except:
                    pass
            if s == 6 and  utime==date == c_date:
                dat = date[:2]
                if int(dat[0]) == 0:
                    dat = dat[-1]
                    print(4)

                m = month[l][int(date[3:5])]
                e_date = str(dat) + ' ' + str(m)
                print(str(cc))
                cc = str(cc)
                cc = cc[:2]
                print(12)
                try:
                    if l == 1:
                        context.bot.send_message(chat_id=e, text=dct[1][17].format(time, f_ru))
                    if l == 2:
                        context.bot.send_message(chat_id=e, text=dct[l][17].format(time,f_uz))
                    try:
                        workbook = xlsxwriter.Workbook('user_exel_list.xlsx')
                        ids = cur.execute('''
                                    SELECT TG_ID
                                    FROM Users
                                    WHERE TG_ID !=0
                                    ''').fetchall()
                        nam = cur.execute('''
                                    SELECT F_name
                                    FROM Users
                                    ''').fetchall()
                        te = cur.execute('''
                                    SELECT Phone_Num
                                    FROM Users
                                    ''').fetchall()
                        bday = cur.execute('''
                                    SELECT UDATA
                                    FROM Users
                                    ''').fetchall()
                        moment = cur.execute('''
                                    SELECT DATA_M
                                    FROM Book
                                    ''').fetchall()
                        baby = cur.execute('''SELECT B_STAGE 
                                              FROM Users
                                              ''').fetchall()

                        dd = []
                        for e in ids:
                            e = e[0]

                        id = []
                        name = []
                        tel = []
                        tow = []
                        lan = []
                        babys = []
                        for i in range(len(ids)):
                            id.append(ids[i][0])

                            name.append(nam[i][0])
                            tel.append(te[i][0])
                            lan.append(moment[i][0])
                            tow.append(bday[i][0])
                            babys.append(baby[i][0])

                        df = pd.DataFrame({'TG_ID': id,
                                           'Исми': name,
                                           'Телефон раками': tel,
                                           'Бола синфи': babys,
                                           'Очик эшиколар куни': tow})
                        df.to_excel('user_exel_list.xlsx', sheet_name='Statistika', index=False)

                        context.bot.send_document(document=open('user_exel_list.xlsx', 'rb'),
                                                  filename='Статисткиа_последняя.xlsx',
                                                  caption='Статистика', chat_id=adct[0])
                    except Exception:
                        context.bot.send_message(chat_id=adct[0], text='Нимадур нотогри йоки таблица бош!!!!)))')

                    cur.execute(stagee.format('{}', e).format(7))
                    cur.execute("""DELETE FROM Users WHERE TG_ID = {} """.format(e))
                    cur.execute("""DELETE FROM Book WHERE TG_ID = "{}" """.format(e))
                    connect.commit()
                except:
                    pass
    if int(now[:2]) ==7:
        for e in all_users:
            e=e[0]
            s = cur.execute("""SELECT Stage FROM Users WHERE TG_ID= "{}" """.format(e)).fetchall()
            utime = cur.execute(select_BOOKDATA.format(e)).fetchall()

            try:
                utime = utime[0][0]
                s = s[0][0]
            except :
                print('klizmaaa')

            if s == 7 and utime ==  date:
                cur.execute(stagee.format(6, e))
                connect.commit()




def get_contac(update, context):
    user_id = update.message.chat_id
    num = update.message.contact.phone_number
    num = str(num)
    conn = sqlite3.connect('users.sqlite')
    cur = conn.cursor()
    cur.execute(update_phone_num.format(num, user_id))
    cur.execute(stagee.format('{}', user_id).format(5))
    lang_ = cur.execute(lang_select.format(user_id)).fetchall()
    conn.commit()

    lang_ = lang_[0][0]
    k_but = [KeyboardButton(text='далее>>>')]
    context.bot.send_message(chat_id=user_id, text=dct[lang_][4], reply_markup=ReplyKeyboardRemove([k_but]))

