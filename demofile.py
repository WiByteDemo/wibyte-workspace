import colorama
from colorama import Fore, Back, Style
import pyfiglet

print('Hello', 'World', 'How', 'are', 'you?', sep = '\v')

input()

# colorama

print()
print(Style.BRIGHT, end = '')
print(Fore.GREEN + 'The world is full of colors')
print(Fore.RED + 'Hello', end = ' ')
print(Fore.BLUE + 'World!')

print(Style.RESET_ALL)

# pyfiglet
print('and now Pyfiglet')
print(Fore.YELLOW, end = '')

result = pyfiglet.figlet_format('Hello World', font = 'bubble')
print(result)

# turtle

import turtle
t = turtle.Turtle()
t.shape('turtle')

t.pencolor('green')
t.write('Hello World!', move = False, align = 'left', font = ('Verdana', 18, 'italic'))
turtle.mainloop()