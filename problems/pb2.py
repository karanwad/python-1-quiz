def max_values(nums):
  list = []

  # max_num = max(nums)
  # list.append(max_num)
  # print(list)


  # return list[0]

  # num1 = nums.index(max(nums))
  # list.append(num1)

  max_val = nums.index(max(nums))
  list.append(max_val)
  for i in range(1, len(nums)):
    if(nums[i] > max_val):
      max_val = nums[i]
     

  return list 


print(max_values([4, 7, 2, 8, 10, 9])) # -> [4, 5]
print(max_values([-5, -2, -1, -11])) # -> [1, 2]