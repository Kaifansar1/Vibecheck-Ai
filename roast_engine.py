import random

roasts = [
    

    # 🔥 DARK + NSFW + Savage Roasts (⚠️ for friends only)
    # ---------------------------------------------------------------
    # 🚫 WARNING: These roasts contain dark humor.
    

    "You bring less excitement than a sock during solo time.",
    "Your love life is like expired milk — sad, sour, and smells funny.",
    "You're the reason people fake moans.",
    "You're like foreplay with gloves on — awkward and unnecessary.",
    "You're about as satisfying as a sneeze that doesn't come.",
    "You couldn’t turn on a light, let alone a person.",
    "You're the reason the 'ick' exists.",
    "You're like a broken vibrator — loud and useless.",
    "Your bedroom game is like a buffering video — starts fast, ends in disappointment.",
    "You're so dry, even Sahara would hand you lotion.",
    "You're like the 'are you still watching?' prompt — ruining the mood every time.",
    "You're the reason 'it’s not size, it’s effort' had to be said.",
    "You're not a snack. You're that thing stuck in my teeth all day.",
    "You're like a bra at home — unnecessary and better off forgotten.",
    "You're the foreplay version of small talk: boring and done out of obligation.",
    "You're like a 2-minute microwave meal — quick, hot, and unsatisfying.",
    "You're like morning wood — annoying and gone in seconds.",
    "Your vibe is like a public bathroom — no one wants to be there, but sometimes it’s an emergency.",
    "You're the plot twist no one wanted — or asked for."
    # ---------------------------------------------------------------
]

def generate_roast(name):
    return f"{name}, {random.choice(roasts)}"