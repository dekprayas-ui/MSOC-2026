rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))

matrix = []

print("Enter matrix:")

for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(cols):
    for j in range(rows):
        print(matrix[j][i], end=" ")
    print()

primary_sum = 0
secondary_sum = 0

if rows == cols:
    for i in range(rows):
        primary_sum += matrix[i][i]
        secondary_sum += matrix[i][rows - 1 - i]

    print(primary_sum)
    print(secondary_sum)
else:
    print("Diagonal sum not possible")