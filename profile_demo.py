#!/usr/bin/env python3

# N.B run using:
# pyflame -o perf.log -x -t ./profile_demo.py
# Create flamge graph using
# flamegraph.pl --title " " --width=1000 perf.log > profile.svg

import time

def main():

    for i in range(50000):
        slow_often_called()
        fast_often_called()

        if(i%280 == 0):
            slow_rarely_called()
            fast_rarely_called()


def slow_often_called():
    time.sleep(0.01)


def fast_often_called():
    pass


def slow_rarely_called():
    time.sleep(3.00)

def fast_rarely_called():
    pass


if __name__ == "__main__":
    main()
