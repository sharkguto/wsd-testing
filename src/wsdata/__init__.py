#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# __init__.py
# @Author : Gustavo Freitas (gustavo@gmf-tech.com)
# @Link   : 
# @Date   : 9/30/2019, 3:03:03 PM


from sys import stdout
from time import sleep

# Count from 1 to 10 with a sleep
while True:
    for count in range(0, 10):
        print(count + 1)
        stdout.flush()
        sleep(0.5)
    print("clean")

