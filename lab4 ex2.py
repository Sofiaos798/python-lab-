n = 7

arr = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        val = i + j + 1  # основна формула
        if val <= n:     # поки не виходить за межі 7
            arr[i][j] = val
        else:
            arr[i][j] = 0  # решта — нулі

print(f"Результат заповнення масиву {n}x{n}:")
for row in arr:
    print(*row)
