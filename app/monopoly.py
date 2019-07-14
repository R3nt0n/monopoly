#!/usr/bin/env python
# -*- coding: utf-8 -*-
# R3nt0n

from random import randint


class Monopoly():

    position = 0
    place = ""
    places = ["Street 1", "Street 2", "Street 3", "Street 4", "Jail", "Street 5",
              "Street 6", "Hospital", "Street 7", "Street 8", "Street 9"]
    result = ''

    # Moving the box
    def move(self):
        # Generating the dice result
        self.result = randint(0, 6)
        self.position = self.position + int(self.result)
        # Amending the out of ranges in the board
        if self.position >= len(self.places):
            self.position = self.position - len(self.places)

        # Printing info
        # print "Dice throwed... {}".format(self.result)
        # print "Now you are in {}".format(self.places[self.position])


if __name__ == '__main__':
    monopoly = Monopoly()
    monopoly.move()