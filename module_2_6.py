from random import randint


def cipher(n):
    cont = []
    unique = ' '
    for i in range(1, n):
        for j in range(1, n):
            if i + j == n and i != j:
                if [j, i] in cont:
                    continue
                cont.append([i, j])
                unique += str(i) + str(j)
    return f'{n} - {unique}'

n = randint(3, 20)

print('выбор нужного пароля из пары чисел:')

result = cipher(n)
print(result)
