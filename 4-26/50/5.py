song = [
    "I really wanna stop",
    "But l just gotta taste for it",
    "l feel like l could fly with the ball on the moon",
    "So honey hold my hand you like making me wait for it",
    "I feel l could die walking up to the room oh yeah",
    "Late night watching television",
    "But how we get in this position",
    "It's way too soon l know this isn't love",
    "But l need to tell you something",
    "I really really really really really really like you"
]
words = []
for i in song:
    words+=i.split(' ')
words = set(words)
for i in words:
    print(i, end=',')
