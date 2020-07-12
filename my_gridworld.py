#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Apr-22-20 20:59
# @Author  : Kelly Hwong (you@example.org)
# @Link    : http://example.org

import os
# global variables
BOARD_ROWS, BOARD_COLS = 3, 4
WIN_STATE = (0, 3)
LOSE_STATE = (1, 3)
START = (2, 0)
DETERMINISTIC = True


class GridWorld(object):
    def __init__(self):
        self.state = START

    def reward(self):
        if self.state == WIN_STATE:
            return 1
        elif self.state == LOSE_STATE:
            return -1
        else:
            return 0


def main():
    # plot array
    arr = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12]]
    print(arr)


if __name__ == "__main__":
    main()
