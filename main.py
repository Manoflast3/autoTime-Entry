import re
import argparse
import pprint
import pyautogui as pyag
import time

x = 765
y = 307
y_offset = 25
x_offset = 25
# Code works on Google Chrome, on 1920 x 1080 screen.
def enterTimes(foo, bar, qux, vas):
    time.sleep(1)
    pyag.typewrite(foo + '\n')
    pyag.typewrite(bar + '\n')
    pyag.typewrite(qux + '\n')
    pyag.typewrite(vas + '\n')
    # move away
    pyag.click(738, 230)
    time.sleep(0.5)
    return

def main(qux, foo=1, bar=2, vas=3):
    print("Foo: {}\nBar: {}\nQux: {}\nVas: {}".format(foo, bar, qux, vas))
    pp = pprint.PrettyPrinter(indent=4)
    # Monday
    pyag.click(x,307)
    enterTimes(foo, bar, qux, vas)
    # Tuesday
    pyag.click(x-x_offset,343)
    enterTimes(foo, bar, qux, vas)

    pyag.click(x-x_offset,368)
    enterTimes(foo, bar, qux, vas)

    pyag.click(x-x_offset,397)
    enterTimes(foo, bar, qux, vas)

    pyag.click(x-x_offset,426)
    enterTimes(foo, bar, qux, vas)

    return

def _cli():
    parser = argparse.ArgumentParser(
            description=__doc__,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            argument_default=argparse.SUPPRESS)
    parser.add_argument('-f', '--foo', default ="9:00", help="This is the first time to input")
    parser.add_argument('-b', '--bar', default ="11:40", help="This is the second time to input")
    parser.add_argument('-q', '--qux', default = "12:40", help="This is the third time to input")
    parser.add_argument('-v', '--vas', default = "18:00", help="This is the fourth time to input")

    args = parser.parse_args()
    return vars(args)


if __name__ == "__main__":
    main(**_cli())
