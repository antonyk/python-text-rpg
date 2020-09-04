from typing import NamedTuple
import textwrap
from termcolor import colored
# terminal printing

# 1. define message categories
# - pass some text, pass category,


class PrintCategory(NamedTuple):
    name: str
    color: str
    bgcolor: str
    attr: str


class TPrint:

    def send(message, category):
        print(colored(message, category.color, ))
        pass


class PrintCategories:
    error = PrintCategory(name='error', color='red', bgcolor='white', attr='')
    roomdesc = PrintCategory(
        name='roomdesc', color='red', bgcolor='white', attr='')
    infohead = PrintCategory(
        name='infohead', color='red', bgcolor='white', attr='')
    info = PrintCategory(name='info', color='red', bgcolor='white', attr='')


pc = PrintCategories()


cats = {
    "error": {
        color: "red",
        bgcolor: "white",
    }
}

cat = cats['error']
cat[color]

# termcolor module settings:
# Text colors:
#   grey
#   red
#   green
#   yellow
#   blue
#   magenta
#   cyan
#   white

# Text highlights:
#   on_grey
#   on_red
#   on_green
#   on_yellow
#   on_blue
#   on_magenta
#   on_cyan
#   on_white

# Attributes:
#   bold
#   dark
#   underline
#   blink
#   reverse
#   concealed
