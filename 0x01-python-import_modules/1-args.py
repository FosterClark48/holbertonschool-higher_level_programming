#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = len(sys.argv) - 1
    if arg == 0:
        print("{:d} arguments.".format(arg))
    elif arg == 1:
        print("{:d} argument:".format(arg))
    else:
        print("{:d} arguments:".format(arg))
    for i in range(arg):
        print("{:d}: {} ".format(i + 1, sys.argv[i + 1]))
