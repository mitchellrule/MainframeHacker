from time import sleep


def hack_moodle():
    print "Found object 'Bernd.Dremel.profile.exe'\nOpening object...\n"
    sleep(2)
    moodle = open("moodle.txt")
    moodle_text = moodle.read()
    moodle_lines = moodle_text.split('\n')

    for line in moodle_lines:
        print line
        sleep(0.01)