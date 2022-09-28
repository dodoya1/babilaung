import re
from pykakasi import kakasi
import pyttsx3
import time

# オブジェクトをインスタンス化
kakasi = kakasi()
s = pyttsx3.init()

#解答して不正解の回数(グローバル変数)
miss_count=0

#メインの関数。バビ語に変換した後、音声出力する関数(正解だった場合実行する)
def lambda_handler(text1):
    #バビ語を音声に
    s.say(text1)  
    s.runAndWait()

#メインの関数。バビ語に変換した後、音声出力する関数(正解だった場合実行する)
def answer(text1):
    #ひらがなに変換
    text2=toHira(text1)
    #バビ語に変換
    text=tobabi(text2)
    #バビ語に変換した文字列を出力
    return text

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

#ストップウォッチの関数
def convert(sec):
    minits = sec // 60
    second = sec % 60
    milli_sec = (second - int(second)) * 1000
    hour = minits // 60
    min = minits % 60
    return f"{int(hour)}:{int(min)}:{int(second)}:{int(milli_sec)}"

#解答があっているかの関数。
def judge(response):
    #グローバル変数を使うことを再宣言
    global miss_count

    #解答が正解の場合
    if answer(text)==response:
        #ストップウォッチを止める。
        stop_time = time.time()
        #ストップウォッチの結果(正解までにかかった時間)を出力。
        result = stop_time - start_time
        time_result = convert(result)
        print(f"正解！かかった時間は：{time_result}です。")
        #正解の場合、バビ語に変換した文字列を音声で出力。
        lambda_handler(response)
        return 0
    #不正解の場合
    else:
        #解答して不正解の回数(グローバル変数)
        miss_count+=1
        if miss_count==3:
            print("残念!不正解です。解答チャンスが0回になりました。また遊んでね!")
            return 0
        print(f"不正解です。あと{3-miss_count}回解答できます")
        #もう一度入力を受け取り、解答があっているかの関数を実行する。
        judge(input())

#ユーザーがエンターを押すとストップウォッチが開始され、問題文が出力される。
start_signal = input("エンターを押すと問題文が出力されます。同時にストップウォッチが開始されます。解答権は3回です。")
#問題出力
print("以下の言葉をバビ語に変換して下さい。")

#問題(ここに問題文を入れる。)
text="はじめまして"
print(text)
#ストップウォッチを開始する。
start_time = time.time()

#解答が正解かを判定する関数を実行。
judge(input())