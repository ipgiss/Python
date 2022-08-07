'''
Напишите программу, которая вычисляет процентное содержание символов G (гуанин) и C (цитозин) в введенной строке
(программа не должна зависеть от регистра вводимых символов).


Sample Input:

acggtgttat
Sample Output:

40.0
'''

# put your python code here
s = input()
s = s.lower()
cnt1 = 0  # C+G
cnt2 = len(s)  # длина строки
for nucl in s:
    if nucl == 'g' or nucl == 'c':
        cnt1 += 1
# print(cnt1, cnt2, end=' ') # это я для себя, для проврки правильности нахождения символов
print(cnt1 / cnt2 * 100)