import time

def calculate_time(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        run = end_time - start_time
        print(f'Total time {run}')
    return wrapper
