#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# __init__.py
# @Author : Gustavo Freitas (gustavo@gmf-tech.com)
# @Link   : 
# @Date   : 9/30/2019, 3:03:03 PM


from sys import stdout, stdin
from time import sleep




# # Count from 1 to 10 with a sleep
# while True:
#     for count in range(0, 10):
#         print(count + 1)
#         stdout.flush()
#         sleep(0.5)
#         line = stdin.readline().strip()
#         print('Hello %s!' % line)
#         stdout.flush() # Remember to flush
        
#     print("clean")




def something(line):
  print('read input:', line, end='',flush=True)


def something_else(count):
    print(count + 1,flush=True)
    sleep(0.5)

# If there's input ready, do something, else do something
# else. Note timeout is zero so select won't block at all.

