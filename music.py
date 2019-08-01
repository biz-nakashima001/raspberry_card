#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import array
import pyaudio
import time


def tone(freq, sec=1, velocity=.2, rate=44100):
    w = rate / freq
    def gen():
        for i in xrange(int(rate * sec)):
            yield math.sin(float(i % w) / w * 2. * math.pi) * velocity
    return array.array('f', gen()).tostring()

def hello():
    music(1)

def goodby():
    music(2)

def kigen():
    music(3)

def music(type=1):
    p = pyaudio.PyAudio()
    stream = p.open(rate=44100, channels=1, format=pyaudio.paFloat32, output=True)

    scale = [ 
        261.63, # C
        293.66, # D
        329.63, # E
        349.23, # F
        392.00, # G
        440.00, # A
        493.88, # H
        261.63 * 2, # C
    ]

    if type==1:
        stream.write(tone(scale[5] * 8, sec=.2))
        # time.sleep(1)
    elif type==2:
        stream.write(tone(scale[5] * 8, sec=.2))
        stream.write(tone(scale[5] * 8, sec=.2))
        # time.sleep(1)
    elif type==3:
        stream.write(tone(scale[5] * 8, sec=.8))
        # time.sleep(1)

    stream.close()
    p.terminate()

