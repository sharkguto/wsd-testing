#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# __main__.py
# @Author : Gustavo Freitas (gustavo@gmf-tech.com)
# @Link   :
# @Date   : 9/30/2019, 5:02:33 PM
import sys
import select
from random import randint
from . import receive_command_from_client, sending_to_client, check_auth
from datetime import datetime

if __name__ == "__main__":
    check_auth()

    while True:

        while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            line = sys.stdin.readline()
            if line:
                receive_command_from_client(line)
            else:  # an empty line means stdin has been closed
                print("eof")

        else:
            pass
            sending_to_client(datetime.now())

