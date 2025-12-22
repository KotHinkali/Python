def is_symmetric(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j]!=matrix[j][i]:
                return False
    return True

n=int(input())
mass=[list(map(int, input().split())) for i in range(n)]
print('Симметричен' if is_symmetric(mass) else 'не симметричен')
