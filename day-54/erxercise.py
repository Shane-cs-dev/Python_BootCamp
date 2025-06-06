import time

# print(current_time)  # seconds since Jan 1st, 1970


# Write your code below 👇
def speed_calc_decorator(function):
    def delay():
        current_time = float(time.time())
        function()
        first_time = float(time.time())
        time_ = first_time - current_time
        print(f"{function.__name__} run speed: {time_}")
    return delay

@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    time.sleep(2)
    for i in range(10000000):
        i * i

fast_function()
slow_function()
