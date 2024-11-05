def removeDuplicates(nums):
    numMap = {}

    for num in nums:
        if num in numMap:
            numMap[num] +=1
        else:
            numMap[num] = 1
    updatedList = list(numMap.keys())
    for i in range(0, len(updatedList)):
        nums[i] = updatedList[i]
    
    return len(updatedList)