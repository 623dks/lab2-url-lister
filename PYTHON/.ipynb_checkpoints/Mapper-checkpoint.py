#!/usr/bin/env python3
import sys, re

href_pattern = re.compile(r'href="([^"]+)"')

for line in sys.stdin:
    for url in href_pattern.findall(line):
        print(f"{url}\t1")
