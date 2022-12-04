def twoNumberSum(array, targetSum):
    # Write your code here.

    if(len(array) == 0):
        return []
    
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            if j == i:
                continue

            if (array[i] + array[j]) == targetSum:
                return [array[i], array[j]]

    return []
