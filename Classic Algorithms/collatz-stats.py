# Collatz Conjecture Stats
# Start with a number n > 1. Find the number of steps it takes to reach one using
# the following process: If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.

# This script prints a bar chart showing how many steps each number takes to reach 1.

from Tkinter import *

def collatz(num, steps):

  if num % 2 == 0:
    num /= 2
  else:
    num *= 3
    num += 1

  steps += 1

  if num != 1:
    return collatz(num, steps)

  return steps

# Start the graphic environment
master = Tk()
w = Canvas(master, width = 1900, height = 1000)
w.pack()

for i in range(1, 1900):
  steps = collatz(i, 0)
  w.create_line(i + 2, 940, i + 2, 940 - steps, fill = "black")

mainloop()