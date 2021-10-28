num = int(input())
F = [1, 2, 3]
for n in range(3, num):
    F.append(F[n - 3]+F[n - 2] + F[n - 1])
print(*F)
