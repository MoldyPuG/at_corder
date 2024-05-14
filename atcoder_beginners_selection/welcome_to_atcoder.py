'''
高橋君はデータの加工が行いたいです。

整数 a,b,cと、文字列 s が与えられます。a+b+c の計算結果と、文字列 s を並べて表示しなさい。
'''

a = int(input())
b, c = map(int, input().split())
s = input()

p = a + b + c

print(p, s)