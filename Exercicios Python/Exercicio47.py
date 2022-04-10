print(' ==== Desafio 47 ==== ')

import emoji
from time import sleep

for c in range(10, 0, -1):
    sleep(1)
    print(c)

print(emoji.emojize(':fireworks: :fireworks: BOOOOOM!!! :fireworks: :fireworks: ', language='alias'))
