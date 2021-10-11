import schedule
import time


def test_func():
    print(f"test called at {time.time()}")


def test_func2():
    print(f"test 2 called at {time.time()}")


if __name__ == '__main__':
    schedule.every(1).seconds.do(test_func)
    schedule.every(3).seconds.do(test_func2)

    while True:
        schedule.run_pending()