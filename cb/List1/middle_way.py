def middle_way(a, b):
  return [a[1], b[1]]

print(middle_way([1, 2, 3], [4, 5, 6]))
print("...should be [2, 5]")

print(middle_way([7, 7, 7], [3, 8, 0]))
print("...should be [7, 8]")

print(middle_way([5, 2, 9], [1, 4, 5]))
print("...should be [2, 4]")
