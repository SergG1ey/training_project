import datetime
import time

def decor_fun(func):
    def time_stop():
        print("what_time_is_it_now()")
        time.sleep(3)
        func()
    return time_stop()

@decor_fun
def my_time():
    time_now = datetime.datetime.now()
    print(time_now.strftime("%H:%M"))
