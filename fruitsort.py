def rev(l):
    return l[::-1]

fruits = ['apple', 'strawberry', 'honeydew', 'banana', 'fig', 'cherry']

print('fruits =', fruits, '\n')
print('sorted(fruits)\n', sorted(fruits), '\n\n')
print('sorted(fruits, key=rev)\n', sorted(fruits, key=rev))
