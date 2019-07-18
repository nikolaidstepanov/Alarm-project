import main
from threading import Thread
from tkinter import *
from tkinter import messagebox as mb

Flag = -1
FutMonth = main.FutureTimer.FutureMonth
FutDay = main.FutureTimer.FutureDay
FutHour = main.FutureTimer.FutureHour
FutMinute = main.FutureTimer.FutureMinute


def box():
    global window
    global drawing
    global main_menu

    window = Tk()
    window["bg"] = "#FFFACD"
    window.title("Alarm")
    window.geometry("500x300+300+150")
    window.resizable(False, False) #User can not change weight and height of window

    main_menu = Menu(window, tearoff = 0) # tearoff - unpin Menu
    window.config(menu = main_menu)

    drawing = Canvas(window, width=500, height=300, bg="#FFFACD")
    drawing.place(x=0, y=0)

    marking()

    window.mainloop()  # window is open


def marking():
    global FutMonth
    global FutDay
    global FutHour
    global FutMinute

    setting_menu = Menu(main_menu, tearoff = 0) #setting
    setting_menu_next = Menu(setting_menu, tearoff = 0) #change music

    setting_menu_next.add_command(label='Музыка 1', command = main.change_music1)
    setting_menu_next.add_command(label='Музыка 2', command = main.change_music2)
    setting_menu_next.add_command(label='Музыка 3', command = main.change_music3)
    setting_menu_next.add_command(label='Музыка 4', command = main.change_music4)
    setting_menu_next.add_command(label='Музыка 5', command = main.change_music5)
    setting_menu_next.add_command(label='Музыка 6', command = main.change_music6)

    setting_menu.add_cascade(label='Изменить музыку', menu = setting_menu_next)
    main_menu.add_cascade(label='Настройки', menu=setting_menu)

    # Frontend
    colon = Label(window, text=":",
                    bg="#FFFACD",
                    fg="black",
                    width=2,
                    height = 1,
                    font="Arial 16")

    FutMonth = Entry(window, bg="#FFFACD",
                    fg="#A52A2A",
                    bd = 0,
                    cursor = "xterm",
                    width=6,
                    font="Arial 16")

    FutDay = Entry(window, bg="#FFFACD",
                    fg="#A52A2A",
                    bd = 0,
                    cursor = "xterm",
                    width=2,
                    font="Arial 16")

    FutHour = Entry(window, bg="#FFFACD",
                    fg="#A52A2A",
                    bd = 0,
                    cursor = "xterm",
                    width=2,
                    font="Arial 16")

    FutMinute = Entry(window, bg="#FFFACD",
                    fg="#A52A2A",
                    bd = 0,
                    cursor = "xterm",
                    width=2,
                    font="Arial 16")

    TurnAlarm = Button(window, text = "Включить будильник",
                        bg = "#FFFACD",
                        fg = "#A52A2A",
                        bd = 0,
                        cursor = "arrow",
                        width = 10,
                        height = 2,
                        wraplength = 100,
                        command = start,
                        font = "Arial 12")

    TurnAlarmOff = Button(window, text = "Выключить будильник",
                        bg = "#FFFACD",
                        fg = "#A52A2A",
                        bd = 0,
                        cursor = "arrow",
                        width = 10,
                        height = 2,
                        wraplength = 100,
                        command = stop,
                        font = "Arial 12")

    FutMonth.insert(0, main.NowMonth)
    FutDay.insert(0, main.NowDay)
    FutHour.insert(0, main.NowHour)
    FutMinute.insert(0, main.NowMinute)

    #marking
    FutMonth.place(x=220, y=102)
    FutDay.place(x=190, y=102)
    FutHour.place(x=205, y=130)
    FutMinute.place(x=240, y=130)
    colon.place(x=220, y=128)
    TurnAlarm.place(x=130, y=180)
    TurnAlarmOff.place(x=240, y=180)

    #button borders
    drawing.create_rectangle(129, 179, 227, 227, outline="#A52A2A")
    drawing.create_rectangle(239, 179, 337, 227, outline="#A52A2A")
    drawing.create_rectangle(120, 90, 346, 240, outline="#A52A2A")


def turnAlarmOff():
    main.alarm_stop()
    mb.showinfo("Статус будильника", "Будильник выключен")

    main.now = main.datetime.datetime.now()
    main.NowMonth = main.now.month
    main.NowDay = main.now.day
    main.NowHour = main.now.hour
    main.NowMinute = main.now.minute
    main.NowMonth, main.NowHour, main.NowMinute = main.get_correct_time(main.NowMonth, main.NowHour, main.NowMinute)

    global FutMonth
    global FutDay
    global FutHour
    global FutMinute

    FutMonth.delete(0, 30)
    FutDay.delete(0, 30)
    FutHour.delete(0, 30)
    FutMinute.delete(0, 30)

    FutMonth.insert(0, main.NowMonth)
    FutDay.insert(0, main.NowDay)
    FutHour.insert(0, main.NowHour)
    FutMinute.insert(0, main.NowMinute)


def turnAlarm():
    global FutMonth
    global FutDay
    global FutHour
    global FutMinute

    str_fm = str(FutMonth.get())
    str_fd = str(FutDay.get())
    str_fh = str(FutHour.get())
    str_f_min = str(FutMinute.get())

    error = main.validate_zero(str_fm, str_fd, str_fh, str_f_min)
    if error == 1:
        mb.showerror("Ошибка", "Заполните пустые поля")
        return

    fm = FutMonth.get()
    fm = main.get_month(fm)
    fd = int(FutDay.get())
    fh = int(FutHour.get())
    f_min = int(FutMinute.get())

    if fm == -2:
        mb.showerror("Ошибка", "Некорректно введен месяц")
        return

    error = main.validate_correct(fm, fd, fh, f_min, str_fd, str_fh, str_f_min)
    if error == 3:
        mb.showerror("Ошибка", "Некорректно введено число месяца")
        return
    elif error == 4:
        mb.showerror("Ошибка", "Некорректно введен час")
        return
    elif error == 5:
        mb.showerror("Ошибка", "Некорректно введены минуты")
        return

    main.FutureTimer.FutureMonth = fm

    main.FutureTimer.FutureDay, main.FutureTimer.FutureHour, main.FutureTimer.FutureMinute = \
        main.FutureTimer.set_time_alarm(fd, fh, f_min)

    error = main.CurrentTime.validate_now_time(main.FutureTimer.FutureMonth, main.FutureTimer.FutureDay,
                                               main.FutureTimer.FutureHour, main.FutureTimer.FutureMinute) #The comparison
                                                                                                    # with the current time
    if error == 6:
        mb.showerror("Ошибка", "Установленное время меньше, чем текущее")
        return

    mb.showinfo("Статус будильника", "Будильник включен")

    main.FutureTimer.alarm_clock(main.FutureTimer.FutureMonth, main.FutureTimer.FutureDay, main.FutureTimer.FutureHour,
                                 main.FutureTimer.FutureMinute)


def stop():
    global Flag
    Flag = 0
    treadTurnAlarmOff = Thread(target=turnAlarmOff)
    treadTurnAlarmOff.start()


def start():
    global Flag
    Flag = 1
    threadTurnAlarm = Thread(target=turnAlarm)
    threadTurnAlarm.start()


if __name__ == '__main__':
    box()
