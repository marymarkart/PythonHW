import time

def calculate_time(func):
    start_time = time.time()
    func()
    end_time = time.time()
    run = end_time - start_time
    print("Total time " + run)

