def find(s, n):
# write your implementation here
    seen = {}  
    for i, num in enumerate(s):
        c = n - num
        if c in seen:
            print([seen[c], i])
        seen[num] = i
    return None


if __name__=="__main__":
    x=input("please input array: ")
    listx=x.split(",")
    listx=[int(listx[i]) for i in range(len(listx))]
    target=int(input("please input the target: "))
    find(listx,target)



"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Your solution need not be the most efficient one. Of course you are encouraged to come out with the most efficient solution
"""