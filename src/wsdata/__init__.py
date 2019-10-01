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
import jwt
from datetime import datetime

query = os.environ.get("QUERY_STRING", None)

if not query:
    print("Missing key", flush=True)
    os.exit(0)

keys_data = dict(pair.split("=") for pair in query.split("&"))

if not "key" in keys_data:
    print("Missing key", flush=True)
    os.exit(0)

AUTHENTICATE = False
MASTER_KEY = {"gustavo": "zaq12wsxcde3", "gustavo2": "cde34rfvbgt5"}
CLIENT_KEY = {"gustavo": ["gmftech", "gmf-ia"], "gustavo2": ["gmf-ia", "balance"]}

USER_TOKEN = jwt.decode(keys_data["key"], verify=False, algorithm="HS256")


def check_auth():
    global USER_TOKEN

    USER_TOKEN = jwt.decode(
        keys_data["key"],
        MASTER_KEY[USER_TOKEN["username"]],
        verify=True,
        algorithm="HS256",
    )
    USER_TOKEN["exp"] = datetime.fromtimestamp(USER_TOKEN["exp"])

    if not USER_TOKEN["client"] in CLIENT_KEY[USER_TOKEN["username"]]:
        print(f'Access denied! {USER_TOKEN["client"]}', flush=True)
        exit(2)


def receive_command_from_client(line):
    print("read input:", line, end="", flush=True)


def sending_to_client(dt: datetime):
    global AUTHENTICATE

    if not AUTHENTICATE:
        AUTHENTICATE = True
        print(f'expire at {USER_TOKEN["exp"]}', flush=True)

    print(dict(expire_in=str(USER_TOKEN["exp"] - dt)), flush=True)
    sleep(2)

