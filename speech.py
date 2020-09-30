import tkinter as tk
import tkinter.ttk as ttk
import client_io
import jtalk
import json

IP = '192.168.0.xxx'
PORT_WAV = 22222
PORT_POSE = 22223

# Commands for Sota by IIO 
def send_speech(text):
    jtalk.make_wav(text)
    with open('__temp.wav', 'rb') as f:
        data = f.read()
        cli = client_io.MyClient()
        cli.connect(IP, PORT_WAV)
        cli.write(data)
        cli.close()

# Callback: enter key pressed
def callback(e):
    send_speech(t.get())
    t.set('')

# rootメインウィンドウの設定
root = tk.Tk()
root.title("Speech")

# メインフレームの作成と設置
frame = ttk.Frame(root, padding=20)

# 各種ウィジェットの作成
t = tk.StringVar()
entry = ttk.Entry(frame, textvariable=t, width=50)
entry.bind('<Return>', callback)

# レイアウト
frame.pack()
entry.pack(side=tk.LEFT)

# ウィンドウの表示開始
root.mainloop()