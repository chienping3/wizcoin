def rotate(nums, k):
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums
   
   


def rotates(matrix):
    length = len(matrix)
    for i in range(length):
        for j in range(i+1, length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(length):
        matrix[i].reverse()
    return matrix
    
if __name__ == '__main__':
    nums = list(range(1, 9))
    k = 3
    rotate(nums, k)
    print(nums)