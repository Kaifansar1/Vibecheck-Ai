import random

roasts = [
    "You're like a cloud. When you disappear, it's a beautiful day.",
    "You're proof that even evolution takes breaks.",
    "You're not stupid; you just have bad luck thinking.",
    "You have something on your chin... no, the third one down.",
    "You're like a software update. Whenever I see you, I ignore you.",
    "You're as useless as the 'g' in lasagna.",
    "You bring everyone so much joy... when you leave the room.",
    "You have something on your face: intelligence. Just kidding, it's gone.",
    "You’re the reason they put instructions on shampoo bottles.",
    "You're like a WiFi signal in the basement—weak and disappointing.",
    "You're the human version of a participation trophy.",
    "You're the AI's favorite test case: always crashing!"
]

def generate_roast(name):
    return f"{name}, {random.choice(roasts)}"
