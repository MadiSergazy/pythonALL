#######1ESEP ESEP ESEP ESEP ESEP
with open('matrix.txt') as file1:
    su = []
    while True:
        # считываем строку
        line = file1.readline()
        # прерываем цикл, если строка пустая
        if not line:
            break
        # выводим строку
        print(line.strip())
        su.append(line.strip().split())
print(su)
sum = 0
for i in su:
    for j in i:
        sum += int(j)
print(f"SUMMA {sum}")
with open('answer.txt', 'w') as file1:
    for i in su:
        file1.writelines(f'{i} \n')



with open('answer.txt', 'a') as file1:
    file1.write(f'SUMMA: {sum}')
    # закрываем файл
file1.close()



