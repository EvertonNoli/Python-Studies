values = []

for i in range(5):
    value = input("Type a value:")
    values.append(value)

noRepeat = set(values)

print(noRepeat)
