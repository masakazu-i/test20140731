#!/usr/bin/env python

import sys


def readints():
    return map(int, sys.stdin.readline().strip().split(" "))


def main():
    n = readints()[0]
    process(n)


def process(n):
    if n > 0:
        x = readints()[0]
        y = readints()[:x]
        print sum(map(lambda x: max(0, x) ** 2, y))
        process(n - 1)


if __name__ == '__main__':
    main()
