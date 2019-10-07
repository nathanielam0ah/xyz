#!/usr/bin/env python3

from datetime import date, datetime

def Logging (filename, error):

    f = open(filename, 'a+')
    f.write(str(error) + "\n")
    f.close()