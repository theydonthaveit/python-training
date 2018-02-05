"""A basic (single function) API written using hug"""
import hug


@hug.get('/hug_test')
def happy_birthday(name, age:hug.types.number=1):
    """Says happy birthday to a user"""
    return "Happy {age} Birthday {name}!".format(**locals())

@hug.get('/greet/{event}')
def greet(event: str):
    """Greets appropriately (from http://blog.ketchum.com/how-to-write-10-common-holiday-greetings/)  """
    greetings = "Happy"
    if event == "Christmas":
        greetings = "Merry"
    if event == "Kwanzaa":
        greetings = "Joyous"
    if event == "wishes":
        greetings = "Warm"

    return "{greetings} {event}!".format(**locals())

@hug.get('/echo', versions=1)
def echo(text):
    return text


@hug.get('/echo', versions=range(2, 5))
def echo_new(text):
    return "Echo: {text}".format(**locals())
