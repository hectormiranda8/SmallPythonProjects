"""
If you are of a certain age, you’ll remember 
those ancient technological devices called 
DVD players. When not playing DVDs, they 
would display a diagonally traveling DVD logo 
that bounced off the edges of the screen. This program 
simulates this colorful DVD logo by making it 
change direction each time it hits an edge. We’ll also 
keep track of how many times a logo hits a corner of 
the screen. This creates an interesting visual animation to 
look at, especially for the magical moment 
when a logo lines up perfectly with a corner.
You can’t run this program from your integrated development
environment (IDE) or editor because it uses the bext module. 
Therefore, it must be run from the Command Prompt or
Terminal in order to display correctly. You can find
more information about the bext module at
https://pypi.org/project/bext/
"""

import bext
import random
import time


class BouncingText():
    def __init__(self):
        # bext.resize(1280, 720) # 721 because we're counting on y = 0
        self.width, self.height = bext.size()
        self.corner_hit = 0
        self.x = random.randint(0, self.width)
        self.y = random.randint(0, self.height)
        self.vx = random.choice([1, -1])
        self.vy = random.choice([1, -1])
        self.colors = ['red', 'green', 'yellow', 'blue', 'purple', 'cyan', 'white']
        self.curr_color = 'white'

        bext.fg(self.curr_color)
        bext.bg('black')
        bext.title(f"Corner Hits: {self.corner_hit}")
        bext.hide_cursor()
    
    def xBoundary(self) -> bool:
        if self.x in [0, self.width-3]:
            self.vx *= -1
            return True
        return False
    
    def yBoundary(self) -> bool:
        if self.y in [0, self.height-1]:
            self.vy *= -1
            return True
        return False

    def checkBoundaries(self) -> None:
        if (self.x, self.y) in [(0, 0),
                                (self.width-3, 0),
                                (0, self.height-1),
                                (self.width-3, self.height-1)]:
            self.corner_hit += 1
            bext.title(f"Corner Hits: {self.corner_hit}")

        xHit = self.xBoundary()
        yHit = self.yBoundary()
        if xHit or yHit:
            new_color = random.choice(self.colors)
            while new_color == self.curr_color:
                new_color = random.choice(self.colors)
            bext.fg(new_color)
            self.curr_color = new_color

    def bounceLoop(self) -> None:
        try:
            while True:
                self.x += self.vx
                self.y += self.vy
                self.checkBoundaries()
                bext.goto(self.x, self.y)
                print("DVD", end="")
                time.sleep(1)
                bext.clear()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    bt = BouncingText()
    bt.bounceLoop()