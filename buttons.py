import tkinter as tk
import tkinter.ttk as ttk

import client_io
import jtalk
import json

IP = '192.168.0.xxx'
PORT_WAV = 22222
PORT_POSE = 22223

def send_speech(text):
    jtalk.make_wav(text)
    with open('__temp.wav', 'rb') as f:
        data = f.read()
        cli = client_io.MyClient()
        cli.connect(IP, PORT_WAV)
        cli.write(data)
        cli.close()

def send_pose(msec, pose_map):
    data = dict(msec=msec, map=pose_map)
    cli = client_io.MyClient()
    cli.connect(IP, PORT_POSE)
    cli.write(json.dumps(data).encode('utf-8'))
    cli.close()

# コールバック関数
def say_hello():
    send_speech('こんにちは')

def say_thank():
    send_speech('ありがとう')

def say_bye():
    send_speech('さようなら')

def say_filler():
    send_speech('えっと')

def say_purpose1():
    send_speech('この船は、何をするための船だと思いますか？')

def say_purpose2():
    send_speech('この船は、海の底を掘って、土や岩石を、取るための、船です。')

def say_depth1():
    send_speech('この船のすごいところは、ものすごく、深くまで、掘れるところです。')

def say_depth2():
    send_speech('どのくらいの深さまで、掘れると思いますか？')

def say_depth3():
    send_speech('最大で、7000メートルくらいまで、掘れます。7000メートルって、すごいですよね。')

def say_reason1():
    send_speech('なんのために、海の底を、掘っているんだと、思いますか？')

def say_reason2():
    send_speech('地下深くの、土や岩石を調べることで、地震のメカニズムの解明や、未知の生物の発見に、つながるそうですよ。')

def say_riser_pipe1():
    send_speech('ほら、船の下を、みてください。')

def say_riser_pipe2():
    send_speech('パイプが伸びていますよね。それを、ライザーパイプ、といいます。')

def say_riser_pipe3():
    send_speech('海底まで、何百本も、つなげているんですよ。')

def say_drill_pipe1():
    send_speech('そこの、パイプの、先端部分を、見てください。')

def say_drill_pipe2():
    send_speech('それが、ドリルパイプ、です。')

def say_drill_pipe3():
    send_speech('ドリル、という名前の通り、海底を掘るために、使われます。')

def say_casing_pipe1():
    send_speech('そこの、地面に埋まっているパイプ、を見てください。')

def say_casing_pipe2():
    send_speech('これは、ケーシングパイプ、といいます。')

def say_casing_pipe3():
    send_speech('何のために、使われると思いますか？')

def say_casing_pipe4():
    send_speech('ケーシングパイプは、ほった穴が、壊れないように、保護するために、使われます。')

def say_bit1():
    send_speech('あっちの、大きな金属のかたまり、を見てください。')

def say_bit2():
    send_speech('あれは、何だと思いますか？')

def say_bit3():
    send_speech('あれは、ビットというものです。')

def say_bit4():
    send_speech('ギザギザ、の部分を使って、海底を削っていきます。')

def say_bit5():
    send_speech('ちなみに、この、ビットは、２種類、あります。')

def say_bit6():
    send_speech('なんで、２種類、あるんだと思いますか？')

def say_bit7():
    send_speech('要は、穴をあけるようと、地中の土を取り出すようの、２種類ってことですね。')

def say_bit8():
    send_speech('実際は、地層の硬さに応じて、さらにいろいろ、使い分けます。')

def say_thruster1():
    send_speech('この、船の底を、よく見てください。')

def say_thruster2():
    send_speech('小さなプロペラが、６つついているのがわかりますか？')

def say_thruster3():
    send_speech('これはアジマススラスタといいます。')

def say_thruster4():
    send_speech('アジマススラスタは何に使われていると思いますか？')

def say_thruster5():
    send_speech('同じ場所にとどまるために使われます。')

def say_thruster6():
    send_speech('海の流れや風の力で、船が動かされないようにする必要があるんです。')




# GUIのレイアウト
root = tk.Tk()
root.title("Controller")
root.geometry('400x300')
# ボタン：こんにちは
frame01 = ttk.Frame(root)
frame01.pack(side=tk.TOP,expand=True,fill=tk.BOTH)
tk.Button(frame01, text='こんにちは', command=say_hello).pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
tk.Button(frame01, text='ありがとう', command=say_thank).pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
tk.Button(frame01, text='さようなら', command=say_bye).pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
tk.Button(frame01, text='えっと', command=say_filler).pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
# ボタン：目的
frame02 = ttk.Frame(root)
frame02.pack(side=tk.TOP,expand=True,fill=tk.BOTH)
tk.Button(frame02, text='何をする船？', command=say_purpose1).pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
tk.Button(frame02, text='海の底を掘る船です', command=say_purpose2).pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
# ボタン：掘る
frame03 = ttk.Frame(root)
frame03.pack(side=tk.TOP,expand=True,fill=tk.BOTH)
tk.Button(frame03, text='すごく深くまで掘れます', command=say_depth1).pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
tk.Button(frame03, text='どれくらい掘れる？', command=say_depth2).pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
tk.Button(frame03, text='７０００ｍまで掘れる', command=say_depth3).pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
# ボタン：理由
frame04 = ttk.Frame(root)
frame04.pack(side=tk.TOP,expand=True,fill=tk.BOTH)
tk.Button(frame04, text='なぜ掘る？', command=say_reason1).pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
tk.Button(frame04, text='地震メカニズム解明', command=say_reason2).pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
# ボタン：ライザーパイプ
frame05 = ttk.Frame(root)
frame05.pack(side=tk.TOP,expand=True,fill=tk.BOTH)
tk.Button(frame05, text='船の下を見て', command=say_riser_pipe1).pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
tk.Button(frame05, text='ライザーパイプ', command=say_riser_pipe2).pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
tk.Button(frame05, text='何百本もつないでる', command=say_riser_pipe3).pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
# ボタン：ドリルパイプ
frame06 = ttk.Frame(root)
frame06.pack(side=tk.TOP,expand=True,fill=tk.BOTH)
tk.Button(frame06, text='パイプの先端', command=say_drill_pipe1).pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
tk.Button(frame06, text='ドリルパイプ', command=say_drill_pipe2).pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
tk.Button(frame06, text='海底を掘ります', command=say_drill_pipe3).pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
# ボタン：ケーシングパイプ
frame07 = ttk.Frame(root)
frame07.pack(side=tk.TOP,expand=True,fill=tk.BOTH)
tk.Button(frame07, text='地面に埋まっているパイプ', command=say_casing_pipe1).pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
tk.Button(frame07, text='ケーシングパイプ', command=say_casing_pipe2).pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
tk.Button(frame07, text='何のため？', command=say_casing_pipe3).pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
tk.Button(frame07, text='掘った穴を保護する', command=say_casing_pipe4).pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
# ボタン：ビット１
frame08 = ttk.Frame(root)
frame08.pack(side=tk.TOP,expand=True,fill=tk.BOTH)
tk.Button(frame08, text='あっちの金属の塊', command=say_bit1).pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
tk.Button(frame08, text='あれは何だと思う？', command=say_bit2).pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
tk.Button(frame08, text='ビット', command=say_bit3).pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
tk.Button(frame08, text='海底を削ります', command=say_bit4).pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
# ボタン：ビット２
frame09 = ttk.Frame(root)
frame09.pack(side=tk.TOP,expand=True,fill=tk.BOTH)
tk.Button(frame09, text='ビットは2種類', command=say_bit5).pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
tk.Button(frame09, text='なんで2種類？', command=say_bit6).pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
tk.Button(frame09, text='穴あけと土を取り出す', command=say_bit7).pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
tk.Button(frame09, text='地層の硬さで分ける', command=say_bit8).pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
# ボタン：スラスタ１
frame10 = ttk.Frame(root)
frame10.pack(side=tk.TOP,expand=True,fill=tk.BOTH)
tk.Button(frame10, text='船の底を見て', command=say_thruster1).pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
tk.Button(frame10, text='小さなプロペラが６つ', command=say_thruster2).pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
tk.Button(frame10, text='アジマススラスタ', command=say_thruster3).pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
# ボタン：スラスタ２
frame11= ttk.Frame(root)
frame11.pack(side=tk.TOP,expand=True,fill=tk.BOTH)
tk.Button(frame11, text='何に使われてると思う？', command=say_thruster4).pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
tk.Button(frame11, text='同じ場所にとどまるため', command=say_thruster5).pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
tk.Button(frame11, text='船が風で動かされないように', command=say_thruster6).pack(side=tk.LEFT,expand=True,fill=tk.BOTH)


root.mainloop()