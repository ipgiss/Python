'''
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк.
После последней строки матрицы идёт строка, содержащая только строку "end" (без кавычек, см. Sample Input).

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов первой матрицы на позициях
(i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
'''

# put your python code here
m = []
while True:
    n = input().split()
    if n[0] == 'end':
        break
    else:
        m.append(n)
for i in range(len(m)):
    x = ''
    for j in range(len(m[i])):
        a = int(m[i - 1][j])
        if i == len(m) - 1:
            b = int(m[0][j])
        else:
            b = int(m[i + 1][j])
        c = int(m[i][j - 1])
        if j == len(m[i]) - 1:
            d = int(m[i][0])
        else:
            d = int(m[i][j + 1])
        s = a + b + c + d
        x += str(s) + ' '
    print(x.rstrip())

'''
Sample Input 1:
9 5 3
0 7 -1
-5 2 9
end
Sample Output 1:
3 21 22
10 6 19
20 16 -1

Sample Input 2:
1
end
Sample Output 2:
4
'''