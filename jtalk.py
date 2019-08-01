# coding: utf-8
import subprocess
from datetime import datetime

def jtalk(t):
    open_jtalk = ['open_jtalk']
    mech = ['-x', '/var/lib/mecab/dic/open-jtalk/naist-jdic']
    htsvoice = ['-m', '/usr/share/hts-voice/mei/mei_normal.htsvoice']
    speed = ['-r', '0.9']
    allpass = ['-a', '0.58']
    outwav = ['-ow', 'out.wav']
    cmd = open_jtalk + mech + htsvoice + allpass + speed + outwav
    c = subprocess.Popen(cmd,stdin=subprocess.PIPE)
    c.stdin.write(t)
    c.stdin.close()
    c.wait()
    #aplay = ['aplay','-q','out.wav','-Dhw:1,0']
    aplay = ['sudo','aplay','/home/pi/Documents/mori_card/wav/out.wav']
    wr = subprocess.Popen(aplay)
    wr.wait()

def hello():
    aplay = ['sudo','aplay','/home/pi/Documents/mori_card/wav/hello.wav']
    wr = subprocess.Popen(aplay)
    wr.wait()

def goodby():
    aplay = ['sudo','aplay','/home/pi/Documents/mori_card/wav/goodby.wav']
    wr = subprocess.Popen(aplay)
    wr.wait()

def kigen():
    aplay = ['sudo','aplay','/home/pi/Documents/mori_card/wav/kigen.wav']
    wr = subprocess.Popen(aplay)
    wr.wait()

def mitouroku():
    aplay = ['sudo','aplay','/home/pi/Documents/mori_card/wav/mitouroku.wav']
    wr = subprocess.Popen(aplay)
    wr.wait()


def say_datetime():
    d = datetime.now()
    text = '%s月%s日、%s時%s分%s秒' % (d.month, d.day, d.hour, d.minute, d.second)
    jtalk(text)

if __name__ == '__main__':
    say_datetime()

