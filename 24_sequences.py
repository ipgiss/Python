"""
Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... (число повторяется столько раз, чему равно).
На вход программе передаётся неотрицательное целое число n — столько элементов последовательности должна отобразить программа.
На выходе ожидается последовательность чисел, записанных через пробел в одну строку.

Sample Input:
7
Sample Output:
1 2 2 3 3 3 4
"""

# put your python code here
n = int(input())
count = 0
seq = 1
for i in range(n):
    print(seq, end=' ')
    count += 1
    if count == seq:
        seq += 1
        count = 0