# uncompyle6 version 3.3.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Apr 24 2019, 10:05:31) 
# [GCC 4.2.1 Compatible Android (5058415 based on r339409) Clang 8.0.2 (https://a
# Embedded file name: dg
import os, sys, random, time

def tik():
    titik = [
     '.   ', '..  ', '... ', '....']
    for o in titik:
        print '\r\x1b[1;39m[\x1b[32;1m+\x1b[39;1m] \x1b[1;92mLoading \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)


tik()