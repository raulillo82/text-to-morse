import numpy as np
import sounddevice as sd
from time import sleep

unit = 0.132
freq = 400

def bip(freq, dur, a=0, d=0, s=1, r=0):
    t=np.arange(0,dur,1/44100)
    env=np.interp(t, [0, a, (a+d), dur-r, dur], [0, 1, s, s, 0])
    sound=np.sin(2*np.pi*freq*t)*env
    sd.play(sound, samplerate=44100)
    sd.wait()

def dot():
    bip(freq, unit)

def dash():
    bip(freq, 3*unit)

def space(units):
    sleep(unit*units)
