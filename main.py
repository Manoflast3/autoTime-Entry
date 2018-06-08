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
def enterTimes():
    time.sleep(1)
    pyag.typewrite('9:00\n')
    pyag.typewrite('11:40\n')
    pyag.typewrite('12:40\n')
    pyag.typewrite('18:00\n')
    # move away
    pyag.click(738, 230)
    time.sleep(0.5)
    return

def main(qux, foo=1, bar=2):
    print("Foo: {}\nBar: {}\nQux: {}".format(foo, bar, qux))
    pp = pprint.PrettyPrinter(indent=4)
    # Monday
    pyag.click(x,307)
    enterTimes()
    # Tuesday
    pyag.click(x-x_offset,343)
    enterTimes()

    pyag.click(x-x_offset,368)
    enterTimes()

    pyag.click(x-x_offset,397)
    enterTimes()

    pyag.click(x-x_offset,426)
    enterTimes()

    return

def _cli():
    parser = argparse.ArgumentParser(
            description=__doc__,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            argument_default=argparse.SUPPRESS)
    parser.add_argument('-f', '--foo', help="This is the input shape file argument")
    parser.add_argument('-b', '--bar', help="This is the output shape file argument")
    qux_help = ("This argument will show its default in the help due to "
                "ArgumentDefaultsHelpFormatter")
    parser.add_argument('-q', '--qux', default=3, help=qux_help)
    args = parser.parse_args()
    return vars(args)


if __name__ == "__main__":
    main(**_cli())
