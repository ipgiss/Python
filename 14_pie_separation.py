'''
Между информатиками и биологами устраивается соревнование.
Победителям соревнования достанется большой и вкусный пирог. В команде биологов aa человек, а в команде информатиков — bb человек.
Нужно заранее разрезать пирог таким образом, чтобы можно было раздать кусочки пирога любой команде, выигравшей соревнование,
при этом каждому участнику этой команды должно достаться одинаковое число кусочков пирога.
И так как не хочется резать пирог на слишком мелкие кусочки, нужно найти минимальное подходящее число.

Напишите программу, которая помогает найти это число.
Программа должна считывать размеры команд (два положительных целых числа aa и bb, каждое число вводится на отдельной строке)
и выводить наименьшее число dd, которое делится на оба этих числа без остатка.
'''

# put your python code here
a = int(input())
b = int(input())
d = 1
while d % a != 0 or d % b != 0:
    d += 1
print(d)

'''
Sample Input 1:
1
2
Sample Output 1:
2

Sample Input 2:
7
5
Sample Output 2:
35


Sample Input 3:
15
15
Sample Output 3:
15
'''