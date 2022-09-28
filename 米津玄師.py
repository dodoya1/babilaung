#文字列
s=input()

#出力する新しい文字列。
ans=""

#「。」の出現回数
count=0

#ウェッを挿入する処理。
for i in range(len(s)):
    ans+=s[i]
    if s[i]=="。":
        count+=1
        if count%2==1:
            ans+="ウェッ。"

print(ans)