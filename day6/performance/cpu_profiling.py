import random
import time

# python -m cProfile --sort cumtime cpu_profiling.py


def an_expensive_function():
    execution_time = random.random() / 100
    time.sleep(execution_time)


if __name__ == '__main__':
    for _ in range(1000):
        an_expensive_function()

