import random

def pick_random_word():
    WORDS = ("python", "javascript", "needed", "carrying", "answer", "celestial", "piano")
    word = random.choice(WORDS)
    return word

hidden_word = pick_random_word()
print(hidden_word)

