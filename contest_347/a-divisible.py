'''
正整数N,K及び長さNの数列A=(A1,A2,…,AN)が与えられます。

Aに含まれる要素のうち、Kの倍数であるもののみを全て取り出し、それらをKで割って出力してください。
'''

n, k = map(int, input().split())
a = list(map(int, input().split()))

a_list = []

for i in range(len(a)):
    if a[i] % k == 0:
        a_list.append(int(a[i]/k))

sorted_list = sorted(a_list)
result = [str(i) for i in sorted_list]
print(" ".join(result))
