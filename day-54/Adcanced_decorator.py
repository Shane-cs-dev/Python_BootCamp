class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def decorator(function):
    def wrapper(*args):
        if args[0].is_logged_in:
            return function(args[0])
    return wrapper
@decorator
def create_blog_post(user):
    return f"Hello and welcome {user.name}!"

new_user = User(name="Shane")
new_user.is_logged_in = True
print(create_blog_post(new_user))
