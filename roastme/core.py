import random

roasts = [
    "{name}, You have something on your chin... no, the third one down.",
    "{name}, If I had a dollar for every smart thing you said, I’d be broke.",
    "{name}, You bring everyone so much joy… when you leave the room.",
    "{name}, You have something on your face… oh wait, that’s just your personality.",
    "{name}, You're the reason the gene pool needs a lifeguard.",
    "{name}, I'd agree with you, but then we’d both be wrong.",
    "{name}, You have something money can’t buy… a really punchable face.",
    "{name}, If ignorance is bliss, you must be the happiest person alive.",
    "{name}, I’d explain it to you but I left my crayons at home.",
    "{name}, You're proof that evolution can go in reverse.",
    "{name}, You're like a cloud. When you disappear, it’s a beautiful day.",
    "{name}, You bring nothing to the table — not even the table.",
    "{name}, I envy people who haven't met you.",
    "{name}, If being annoying were a sport, you’d have an Olympic gold by now.",
    "{name}, I thought of you today. It reminded me to take the trash out.",
    "{name}, You have something rare — the ability to annoy in complete silence.",
    "{name}, You're the human equivalent of a typo.",
    "{name}, Even autocorrect can't fix what's wrong with you.",
    "{name}, Your secrets are always safe with me. I never even listen when you tell me them.",
    "{name}, I’m not saying you’re useless, but your WiFi signal is stronger than your personality.",
    "{name}, Your face makes onions cry.",
    "{name}, You’re like a broken pencil… pointless.",
    "{name}, You make sloths look productive.",
    "{name}, If you were any slower, you'd be in reverse.",
    "{name}, You're not the sharpest knife in the drawer. Actually, you're not even in the drawer.",
    "{name}, You have an entire life to be a better person. Don’t waste it.",
    "{name}, I’d say you were born for greatness, but it looks like you overslept.",
    "{name}, If cringe had a face, it would borrow yours.",
    "{name}, You're like software in beta — buggy, unfinished, and nobody asked for you.",
    "{name}, You’re so dense, light bends around you.",
]

def get_roast(name):
    return random.choice(roasts).format(name=name)
