import random

roasts = [
    "{name}, You have something on your chin... no, the third one down.",
    "{name}, If I had a dollar for every smart thing you said, I’d be broke.",
    "{name}, You bring everyone so much joy… when you leave the room.",
    "{name}, You have something on your face… oh wait, that’s just your personality.",
    "{name}, You're the reason the gene pool needs a lifeguard.",
    "{name}, I'd agree with you, but then we’d both be wrong.",
    "{name}, You have something money can’t buy… a really punchable face.",
]

def get_roast(name):
    return random.choice(roasts).format(name=name)
