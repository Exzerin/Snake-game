# wip

import curses

# setup windows
curses.initscr()
win + curses.newin(20, 60, 0, 0) # y,x
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1) # -1

# snake and food
snake = [(4, 10), (4, 9), (4, 8)]
food = ()

# game logic

score = 0

while True:
        event = win.getch()
        # ...
        
curses.endwin()
print(f"Final score= {score}")
