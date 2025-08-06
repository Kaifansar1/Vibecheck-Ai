import random

compliments = [
    "You're like sunshine on a rainy day.",
    "You bring out the best in everyone.",
    "Your smile can light up a whole room.",
    "You're a walking inspiration.",
    "You're proof that kindness is still alive.",
    "You're one of a kind!",
    "You're like a cheat code for happiness.",
    "You're the plot twist everyone needed.",
    "You're smarter than ChatGPT... maybe.",
    "You're the MVP of good vibes.",
    "You're the reason glitter exists.",
    "You're what happens when brilliance meets personality!"
]

def generate_compliment(name):
    return f"{name}, {random.choice(compliments)}"
