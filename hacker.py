__author__ = 'Mitch'

from time import sleep
import sys
from mainframeHacker import hack_the_mainframe
from pentagonHacker import hack_the_pentagon
from moodleHacker import hack_moodle


choices = '''
1. The mainframe
2. The Pentagon
3. Moodle
'''

def choose():
    print "\n" * 100
    print "What would you like to hack?"
    print choices
    choice = raw_input(">")

    if choice == "1":
        hack_the_mainframe()
    elif choice == "2":
        hack_the_pentagon()
    elif choice == "3":
        hack_moodle()
    else:
        print "That wasn't an option oldmate"
        choose()

choose()