import subprocess
import client_io
import os.path

def make_wav(text, output_path=os.getcwd()):
    # Open JTalkをインストールしたパスを指定する。
    OPENJTALK_BINPATH = 'C:\\open_jtalk\\open_jtalk-1.11\\bin'
    OPENJTALK_DICPATH = 'C:\\open_jtalk\\open_jtalk-1.11\\mecab-naist-jdic'
    OPENJTALK_VOICEPATH = 'C:\\open_jtalk\\MMDAgent_Example-1.7\\Voice\\mei\\mei_normal.htsvoice'
    open_jtalk = [OPENJTALK_BINPATH + '/open_jtalk.exe']
    # 以下はraspiにインストールしたときのパスの例
    # OPENJTALK_BINPATH = '/usr/bin'
    # OPENJTALK_DICPATH = '/var/lib/mecab/dic/open-jtalk/naist-jdic'
    # OPENJTALK_VOICEPATH = '/usr/share/hts-voice/mei/mei_normal.htsvoice'
    # open_jtalk = [OPENJTALK_BINPATH + '/open_jtalk']
    mech = ['-x',OPENJTALK_DICPATH]
    htsvoice = ['-m',OPENJTALK_VOICEPATH]
    speed = ['-r','1.0']
    outwav = ['-ow', os.path.join(output_path, '__temp.wav')]
    cmd = open_jtalk + mech + htsvoice + speed + outwav
    c = subprocess.Popen(cmd,stdin=subprocess.PIPE)
    # Windowsで使うときは'shift-jis'で、Linux (raspi)で使うときは'utf-8'に変更する
    c.stdin.write(text.encode('shift-jis'))
    c.stdin.close()
    c.wait()

if __name__ == '__main__':
    make_wav("こんにちは")