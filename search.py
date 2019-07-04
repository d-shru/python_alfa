#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
L2 =[]
L1 = []
L = []



for line in open('/home/shru/tnd/intdoid', 'r'):
    #line = line.rstrip()
    #L.append(line)
    print("++++" + line)

    for linestr in open('/home/shru/tnd/messages', 'r'):
        if line in linestr is True:
            print(linestr)
