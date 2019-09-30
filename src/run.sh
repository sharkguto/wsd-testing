#!/bin/sh
declare -a -g MESSAGES

SCRIPTPATH="$(
    cd "$(dirname "$0")"
    pwd -P
)"

echo $SCRIPTPATH
cd $SCRIPTPATH


websocketd --address=0.0.0.0 --port=80 python3 -m wsdata