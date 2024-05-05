import threading


def print_cube(num):
    print("Cube: {}".format(num * num * num))


def print_square(num):
    print("Square: {}".format(num * num))


if __name__ == "__main__":
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done!")


import threading
import os


def task1():
    print("1-topshiriq ipga tayinlangan: {}".format(threading.current_thread().name))
    print("Jarayonni bajaruvchi vazifa identifikatori 1: {}".format(os.getpid()))


def task2():
    print("2-topshiriq ipga tayinlangan: {}".format(threading.current_thread().name))
    print("Jarayonni bajaruvchi vazifa identifikatori 2: {}".format(os.getpid()))


if __name__ == "__main__":
        print("Asosiy dasturni ishga tushiradigan jarayon identifikatori: {}".format(os.getpid()))

    print("Asosiy mavzu nomi: {}".format(threading.current_thread().name))

    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')

    t1.start()
    t2.start()

    t1.join()
    t2.join()


import time
import threading


def say_hi(name):
    print(f'Hello {name}')
    time.sleep(1)


def func(n):
    for i in range(1, n):
        print(i ** 2)
        time.sleep(1)


t1 = threading.Thread(target=say_hi, args=('Samir',))
t2 = threading.Thread(target=func, args=(5,))

t1.start()
t2.start()

t1.join()
t2.join()









