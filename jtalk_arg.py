# coding: utf-8
import subprocess
import sys

def jtalk(args):
    open_jtalk = ['open_jtalk']
    mech = ['-x', '/var/lib/mecab/dic/open-jtalk/naist-jdic']
    htsvoice = ['-m', '/usr/share/hts-voice/mei/mei_normal.htsvoice']
    valume = ['-jf','1.5'] # 声の大きさ デフォルト1.0
    speed = ['-r', '0.8.'] # スピーチ速度 デフォルト1.0
    sampling = ['-s','50000'] # サンプリング周波数　声の高さ デフォルト auto
    flame = ['-p','240']#フレーム周期　速さ 多いほど遅い デフォルト auto
    allpass = ['-a', '0.60']#オールパス　野太さ 約0.5 以上の大きな値 : 低い声になる約0.5 以下の小さな値 : 高い声になる
    halftone = ['-fm', '1.0']#ハーフトーン　甲高さ
    spectrum = ['-jm', '1.4']#スペクトラム1.0以上の大きな値 : 抑揚が大きくなる　1.0以下の小さな値 : 抑揚が小さくなる
    
    if len(args) > 2:
        filename = str(args[2]) + '.wav'
    else:
        filename = 'out.wav'
    t = args[1]
    outwav = ['-ow', './wav/'+filename]
    cmd = open_jtalk + valume + spectrum + halftone + sampling + flame + mech + htsvoice + allpass + speed + outwav
    # cmd = open_jtalk + mech + htsvoice + outwav
    c = subprocess.Popen(cmd,stdin=subprocess.PIPE)
    c.stdin.write(t)
    c.stdin.close()
    c.wait()
    aplay = ['aplay','./wav/'+filename]
    wr = subprocess.Popen(aplay)
    wr.wait()

if __name__ == '__main__':
    args = sys.argv
    jtalk(args)

