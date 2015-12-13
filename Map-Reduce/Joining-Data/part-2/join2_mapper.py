#!/usr/bin/env python
import sys

# --------------------------------------------------------------------------
# Author : Abhijeet Kandalkar (kandalkar.abhijeet58@gmail.com)
# --------------------------------------------------------------------------

for line in sys.stdin:
    line       = line.strip()       #strip out carriage return
    key_value  = line.split(",")    #split line, into key and value, returns a list
    key_in     = key_value[0]       #.split(" ")   #key is first item in list
    value_in   = key_value[1]       #value is 2nd item 

    #print key_in
    if value_in[0:3] == 'ABC' or value_in.isdigit() :   #if value is ABC or if value is a digit print it out
        print( '%s\t%s' % (key_in, value_in) )

