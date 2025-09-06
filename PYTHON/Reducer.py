#!/usr/bin/env python3
import sys

current_url = None
count = 0

for line in sys.stdin:
    url, val = line.strip().split("\t", 1)
    val = int(val)

    if current_url == url:
        count += val
    else:
        if current_url:
            print(f"{current_url}\t{count}")
        current_url = url
        count = val

if current_url:
    print(f"{current_url}\t{count}")
