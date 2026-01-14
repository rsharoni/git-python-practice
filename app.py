import datetime


def greet(name, time):
    return f"Hello, {name}! the time now is: {time}, Welcome!"


if __name__ == "__main__":
    user = "World"
    time = datetime.datetime.now().strftime("%H:%M:%S")
    print(greet(user, time))
