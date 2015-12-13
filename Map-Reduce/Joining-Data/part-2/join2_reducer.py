#!/usr/bin/env python
import sys

# --------------------------------------------------------------------------
# Author : Abhijeet Kandalkar (kandalkar.abhijeet58@gmail.com)
# --------------------------------------------------------------------------

line_cnt        = 0         #count input lines
abc_found       = False     
running_total   = 0
prev_word       = None

for line in sys.stdin:
    line       = line.strip()       #strip out carriage return
    key_value  = line.split('\t')   #split line, into key and value, returns a list
    line_cnt   = line_cnt+1 

    curr_word  = key_value[0]       #key is first item in list, indexed by 0
    value_in   = key_value[1]       #value is 2nd item

    if curr_word != prev_word:
        if abc_found:
                abc_found = False
                print( "{0} {1}".format(prev_word, running_total) )
                running_total = 0
 
        if value_in != 'ABC':
                running_total = int(value_in)       #reset running count 
    
    else:
        if value_in != 'ABC':
            running_total += int(value_in)      #add value to running total
    
    if value_in == 'ABC':
        abc_found = True

    prev_word = curr_word
