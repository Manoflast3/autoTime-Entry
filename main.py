import re
import argparse
import pprint
import pyautogui as pyag
import time

x = 775
y = 307
y_offset = 28
x_offset = 40
y_start = 248
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
    y = y_start

    # fullscreen it
    pyag.click(800, 307)
    pyag.press('f11')
    # Monday
    pyag.click(x,y)
    enterTimes(foo, bar, qux, vas)
    y = y + y_offset 
    # Tuesday
    pyag.click(x-x_offset,y)
    enterTimes(foo, bar, qux, vas)
    y = y + y_offset 

    pyag.click(x-x_offset,y)
    enterTimes(foo, bar, qux, vas)
    y = y + y_offset 

    pyag.click(x-x_offset,y)
    enterTimes(foo, bar, qux, vas)
    y = y + y_offset 

    pyag.click(x-x_offset,y)
    enterTimes(foo, bar, qux, vas)
    # exit fullscreen
    pyag.press('f11')

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
