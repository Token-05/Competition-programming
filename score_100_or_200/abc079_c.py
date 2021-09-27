S = list(input())

for i in range(2 ** (len(S) - 1)):
    op = ["+"] * 3
    # ビット演算を用いて±の全組み合わせを表現(今回の場合論理積が1の場合-を付与)
    for j in range(3):
        if i >> j & 1:
            op[j] = "-"
    result = S[0] + op[0] + S[1] + op[1] + S[2] + op[2] + S[3]
    if eval(result) == 7: #文字列を式として評価
        print(result + "=7")
        break