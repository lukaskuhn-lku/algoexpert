def isValidSubsequence(array, sequence):
    # Write your code here.
    counter = 0;
    for i in range(0, len(array)):
        if array[i] == sequence[counter]:
            if counter+1 >= len(sequence):
                return True
            else:
                counter += 1    
    
    return False
