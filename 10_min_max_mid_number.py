'''
Напишите программу, которая получает на вход три целых числа, по одному числу в строке, и выводит на консоль в три строки сначала максимальное, потом минимальное,
после чего оставшееся число.
На ввод могут подаваться и повторяющиеся числа.
'''
# put your python code here
a = int(input())
b = int(input())
c = int(input())
s = a + b + c;
print(max(a,b,c))
print(min(a,b,c))
print(s - max(a,b,c) - min(a,b,c))

'''
Sample Input 1:
8
2
14
Sample Output 1:
14
2
8

Sample Input 2:
23
23
21
Sample Output 2:
23
21
23
'''