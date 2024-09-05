a = list(map(int, input("Type number with space: ").split()))
print("a:", a)
n = len(a)
data = int(input("Enter data value that u want to find:"))

for i in range(n):
    if data == a[i]:
        print(f"{data} found at pos {i + 1}")
        break
else:
    print(f"{data} is not found")
