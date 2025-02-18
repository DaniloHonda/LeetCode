def bubble(nums):
  size = len(nums)
  for _ in nums:
    sorted = True
    print(nums)
    for i in range (size-1): # faz com que o loop nao saia do array
      if nums[i] > nums[i+1]:
        nums[i+1], nums[i] = nums[i], nums[i+1] # faz a trade sem precisar de variavel adicional
        sorted = False
    if sorted: # garante que o programa rode ate que o array esteja ordenado
      return
      
nums = [2,5,2,6,3,64,12]
bubble(nums)