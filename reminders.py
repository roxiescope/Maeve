import pystray
import PIL.Image
import Maeve
import os, subprocess, schedule, time, threading, datetime
from plyer import notification
from schedule import every, repeat, run_pending
from winotify import Notification
from utils import todolist_handler

# image = PIL.Image.open("alienpic.png")


# def on_clicked(icon, item):
#     if str(item) == "Say Hello":
#         print("Hello World")
#         # Maeve.main()
#     elif str(item) == "Exit":
#         icon.stop()
#
# def setup(icon):
#     icon.visible = True
#     i=0
#     while icon.visible:
#         Maeve.main()
#         i+=1
#
# def init_icon():
#     icon = pystray.Icon("Maeve", image, menu=pystray.Menu(
#         pystray.MenuItem("Say Hello", on_clicked),
#         pystray.MenuItem("Exit", on_clicked)
#     ))
#     icon.title = 'Maeve'


@repeat(every(30).seconds)
def checkDueTodos():
    #will run every day at 18:00 (6pm)
    #checks if any items in the schedule are past their due date
    print('checking schedule')
    tasks = todolist_handler.getTasksByStatus('open')
    print('Tasks past due:')
    for task in tasks:
        if datetime.datetime.strptime(task.dueDate, '%m/%d/%Y') <= datetime.datetime.now():
            #todo - toast only shows notification on first loop
            toast = Notification(app_id='Maeve',
                                 title=task.name,
                                 msg='task is overdue')
            toast.show()
            print(task.name, ': ', task.summary)


def run_continuously(interval=1):
    # sets up the schedule thread in the background
    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                schedule.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.start()
    return cease_continuous_run


# run the background schedule thread
stop_run_continuously = run_continuously()

# for turning it off
# stop_run_continuously.set()

# if __name__ == '__main__':
#     init_icon()
#     icon.run()


def main():
    checkDueTodos()
