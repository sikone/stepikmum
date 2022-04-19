print('Введите размерность массива:')
n = int(input())
rw = 1
mas = [0] * n 
for i in range(n): 
    mas[i] = [0] * n 
#print(mas) # Выведет [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
iter = 0
rowtmp =0
coltmp=0
while rw <= n*n:                    # логично что максимальное значение это n в квадрате, пока его не будет делаем 4 цикла
    for col in range(iter,n-iter):  #цикл проходит слева направо
        mas[rowtmp][col] = rw
        coltmp = col
        rw +=1
    for row in range(iter+1,n-iter): #Цикл проходит сверху вниз
        mas[row][coltmp] = rw
        rw+=1
        rowtmp = row
    for col in range(rowtmp-1,iter-1,-1): #Цикл проходит справа налево
        mas[rowtmp][col] = rw
        rw+=1
        coltmp=col
    for row in range (n-iter-2,iter,-1): #Цикл прохожит снизу вверх
        mas[row][coltmp] = rw
        rw+=1
        rowtmp=row
    iter+=1
for i in range(0, len(mas)):
    for i2 in range(0, len(mas[i])):
        print(mas[i][i2], end=' ')
    print()
