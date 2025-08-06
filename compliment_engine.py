import random

compliments = [
    "You're doing amazing, {name}!",
    "You're a gift to those around you.",
    "You're someone's reason to smile today.",
    "You're sharper than the edge of Excalibur.",
    "You're brighter than my screen at 3 AM."
]

def generate_compliment(name):
    return random.choice(compliments).replace("{name}", name)