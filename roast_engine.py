import random

roasts = [
    "You're like a cloud. When you disappear, it’s a beautiful day.",
    "Your secrets are safe with me. I never even listen.",
    "You're the reason warning labels exist.",
    "You're not dumb; you just have bad luck thinking.",
    "You're proof evolution pauses sometimes."
]

def generate_roast(name):
    return random.choice(roasts).replace("you", name)