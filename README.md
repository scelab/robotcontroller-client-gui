# robotcontroller-client-gui

Sota (CommU) を遠隔操作するためのGUIツールのサンプルプログラムです。
これを動かすためには、Sota (CommU) の中でRobotControllerが実行されている必要があります。

RobotController: https://github.com/scelab/RobotController

## camera.py

SotaからGstreamerを使って送信された映像と音声を再生します。Sota内でRobotControllerが実行されていれば、映像をクリックすると、ロボットがそのクリックされた点を見るように頭部を動かします。Ctrlを押しながらクリックすると、身体をそちらに向けます。

※Gstreamerを用いてSotaとPCで映像と音声のやり取りをする方法はWikiを参照: https://github.com/scelab/robotcontroller-client-gui/wiki

※このプログラムを利用するには、PC側でopencvとgstreamer、opencv-pythonのインストールが必要です。opencvはgstreamerを利用可能にしないといけないので、再ビルドする必要があります。Ubuntuでの再ビルドは比較的簡単ですが、Windowsでの再ビルドは難しそうです。Ubuntuでのopencvの再ビルドとインストール、gstreamerとopencv-pythonのインストールの方法は、下記URLを参照：
https://dev.classmethod.jp/articles/gstreamer-opencv/

## speech.py

テキストボックスに入力した文字列をjtalk.pyを使って音声合成し、作成された音声ファイルをSotaに送信するプログラムです。Sota内でRobotControllerが実行されていれば、その音声ファイルの内容を発話します。

※このプログラムを利用するには、Open JTalkのインストールが必要です。

## buttons.py

押したボタンのスクリプトを話します。音声はspeech.pyと同じ手順でSotaに送信されています。

## idle.py

アイドルモーションを実行します。

## jtalk.py

Open JTalkを使って音声合成し、音声ファイルを出力するプログラムです。

※このプログラムを利用するには、Open JTalkのインストールが必要です。

## client_io.py

Sota内で実行されるRobotControllerと通信するときに使うクライアントプログラムです。
