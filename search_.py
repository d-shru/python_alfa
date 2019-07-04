#!/usr/bin/env pythin
# -*- coding: utf-8 -*-

import sys, os
L1 = []
L = []

for intdocid in open('/home/shru/tnd/intdoid', 'r'):
    intdocid = intdocid.rstrip()
    L1.append(intdocid)
for linestr in open('/home/shru/tnd/messages', 'r'):
    linestr = linestr.rstrip()
    indx = (linestr.find('status'))
    ind = (linestr.find('trn'))
    if indx > 0 and ind <0:
        for i in L1: 
            if i in linestr: print(linestr)
