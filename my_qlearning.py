#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Apr-22-20 21:08
# @Author  : Kelly Hwong (you@example.org)
# @Link    : http://example.org

import os
import numpy as np

GAMMA = 0.8  # discount factor


def get_max_Q(Q, state):
    return max(Q[state, :])


def QLearning(R, Q, state):
    current_action = None
    for action in range(R.shape[1]):
        if R[state][action] == -1:
            Q[state, action] = 0
        else:
            current_action = action
            Q[state, action] = R[state][action] + \
                GAMMA * get_max_Q(Q, current_action)


def main():
    Q = np.zeros((6, 6))
    R = np.asarray([[-1, -1, -1, -1, 0, -1],
                    [-1, -1, -1, 0, -1, 100],
                    [-1, -1, -1, 0, -1, -1],
                    [-1, 0, 0, -1, 0, -1],
                    [0, -1, -1, 0, -1, 100],
                    [-1, 0, -1, -1, 0, 100]])
    iterations = 1000
    for it in range(iterations):
        for i in range(6):  # i, 假设的初始状态
            QLearning(R, Q, i)
    print(Q/5)


if __name__ == "__main__":
    main()
