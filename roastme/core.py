import random

default_roasts = [
    "You're like a cloud. When you disappear, it's a beautiful day.",
    "You're the reason the gene pool needs a lifeguard.",
    "You have something on your chin... no, the third one down.",
    "You're not stupid; you just have bad luck thinking.",
    "Your code runs like you on a Monday: slow, buggy, and confused.",
    "You're the kind of person who claps when the plane lands.",
    "You bring everyone so much joy… when you leave the room.",
    "If ignorance is bliss, you must be the happiest person alive.",
    "You're like a software update at 3 AM. Nobody asked for you.",
]

def get_roast():
    """Returns a random roast from the default list."""
    return random.choice(default_roasts)

def roast(name):
    """Returns a roast personalized with the given name."""
    return f"{name}, {get_roast()}"
