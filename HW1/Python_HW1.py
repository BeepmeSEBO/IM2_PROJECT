rows = int(input("Enter row: "))
cols = int(input("Enter col: "))

matrix = {}

for r in range(rows):
    row_list = []
    print(f"\nRow {r+1}")
    for c in range(cols):
        num = float(input(f"Enter number{c+1}: "))
        row_list.append(num)
    matrix[r] = tuple(row_list)

print("\nThe numbers are:\n")
for r in matrix:
    print(" ".join(str(x) for x in matrix[r]))

search_num = float(input("\nSearch: "))

found = []
for r in matrix:
    for c in range(len(matrix[r])):
        if matrix[r][c] == search_num:
            found.append((r, c)) 

if found:
    for (r, c) in found:
        print(f"Number {search_num} found at Row {r}, Col {c}")
else:
    print(f"Number {search_num} not found")
