values = []

for i in range(5):
    value = input("Type something:")
    values.append(value)

values.sort()
print(values[::-1])

