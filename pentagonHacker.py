from time import sleep


def hack_the_pentagon():
    print "Beep boop"
    sleep(2)

    for i in range(800):
        print "LAUNCHING NUKES!",
        sleep(0.01)

    print "\n" * 50

    nuke = ('\n'
            '    -----------------------\n'
            '    ----------OO-----------\n'
            '    -------OOOOOOOO--------\n'
            '    ------OOOOOOOOOO-------\n'
            '    ------OOOOOOOOOO-------\n'
            '    ------OOOOOOOOOO-------\n'
            '    -----OOOOOOOOOOOO------    \n'
            '    ------OOOOOOOOOO-------   \n'
            '    ------OOOOOOOOOO-------   \n'
            '    ------OOOOOOOOOO-------    <------- NUKE\n'
            '    ------OOOOOOOOOO-------\n'
            '    ------OOOOOOOOOO-------\n'
            '    ------OOOOOOOOOO-------\n'
            '    ------OOOOOOOOOO-------\n'
            '    ------OOOOOOOOOO-------\n'
            '    ------OOOOOOOOOO-------\n'
            '    ------OOOOOOOOOO-------\n'
            '    ------OOOOOOOOOO-------\n'
            '    -OOOOOOOOOOOOOOOOOOOOO-\n'
            '    OOOOOOOOOOOOOOOOOOOOOOO\n'
            '    OOOOOOOOOOOOOOOOOOOOOOO\n'
            '    OOOOOOOOOOOOOOOOOOOOOOO\n'
            '    OOOOOOOOOOOOOOOOOOOOOOO\n'
            '    -OOOOOOOOOOOOOOOOOOOOO-\n'
            '    -----------------------\n'
            '    ')

    nuke_lines = nuke.split('\n')

    for line in nuke_lines:
        print line
        sleep(0.2)
    for line in range(28):
        print "\n"
        sleep(0.2)