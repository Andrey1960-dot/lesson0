numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [2, 3, 5, 7, 11, 13]
not_primes = [4, 6, 8, 9, 10, 12, 14, 15]
for i in range(2, 16):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
        print(primes)
        print(not_primes)




