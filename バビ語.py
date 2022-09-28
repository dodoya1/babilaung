import re
from pykakasi import kakasi
import pyttsx3

# オブジェクトをインスタンス化
kakasi = kakasi()
s = pyttsx3.init()

#メイン処理。
def lambda_handler(text1):
    #ひらがなに変換
    text2=toHira(text1)
    #バビ語に変換
    text=tobabi(text2)
    #バビ語に変換した文字列を出力
    print(text)
    #バビ語を音声に
    s.say(text)  
    s.runAndWait()

#(漢字やカタカナを)ひらがなに変換する関数
def toHira(text):
    # モードの設定：J(Kanji) to H(Hiragana)
    kakasi.setMode('J', 'H') 
    # 変換して出力
    conv = kakasi.getConverter()
    return conv.do(text)

#バビ語に変換する関数
def tobabi(text):
    rettext=""
    for i in range(len(text)):
        if re.search(text[i],"あかさたなはまやらわんがざだばぱ"):
            rettext+=text[i]+"ば"
        if re.search(text[i],"いきしちにひみりぎじぢびぴ"):
            rettext+=text[i]+"び"
        if re.search(text[i],"うくすつぬふむゆるぐずづぶぷ"):
            rettext+=text[i]+"ぶ"
        if re.search(text[i],"えけせてねへめれげぜでべぺ"):
            rettext+=text[i]+"べ"
        if re.search(text[i],"おこそとのほもよろをごぞどぼぽ"):
            rettext+=text[i]+"ぼ"
    return rettext

#入力を受け取り、メインの関数を実行
lambda_handler(input())