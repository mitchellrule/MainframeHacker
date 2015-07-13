from time import sleep


def hack_the_mainframe():
    text_hacks = open("hacks.txt")
    hacks_string = text_hacks.read()
    lines = hacks_string.split("\n")

    print "Executing mainframe.decompiler...\n"
    sleep(1.5)

    for line in lines:
        print line
        sleep(0.06)

    for i in range(10):
        print "#",
        sleep(0.5)

    print "\n" * 3, "Done, the mainframe has been decompiled.\n\n\n"