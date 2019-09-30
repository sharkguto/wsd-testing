#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# __init__.py
# @Author : Gustavo Freitas (gustavo@gmf-tech.com)
# @Link   :
# @Date   : 9/30/2019, 3:03:03 PM


from sys import stdout, stdin
from time import sleep
import os

query = os.environ.get("QUERY_STRING", None)

if not query:
    print("Missing key", flush=True)
    os.exit(0)

keys_data = dict(pair.split("=") for pair in query.split("&"))

if not "key" in keys_data:
    print("Missing key", flush=True)
    os.exit(0)




# self_name = os.path.basename(__file__)
# if query.startswith(self_name):
#     query = query[len(self_name) + 1 :]


AUTHENTICATE = False
MASTER_KEY = "Pm3HLub6tUBNrp9x"


def check_auth():
    pass


def something(line):
    print("read input:", line, end="", flush=True)


def something_else(count):
    print(query, flush=True)
    # print(count + 1, flush=True)
    sleep(0.5)

