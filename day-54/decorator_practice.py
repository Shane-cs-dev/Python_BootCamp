import time


def nesting_function(function):
    def inner_function():
        time.sleep(1) #Do something before the input function
        function()
        time.sleep(2) #Do sth after the input function
        print("Delay")
    return inner_function

@nesting_function
def say_hello():
    print("hello!")

def say_goodbye():
    print("goodbye")

decorated_function = nesting_function(say_goodbye)
decorated_function()



