def has23(nums):
  if nums[0] == 2 or nums[0] == 3 or nums[1] == 2 or nums[1] == 3:
   return True
  return False

print(has23([2, 5]))
print("...should return True")

print(has23([4, 3]))
print("...should return True")

print(has23([4, 5]))
print("...should return False")
