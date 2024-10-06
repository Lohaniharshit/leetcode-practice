def productExceptSelf1(nums): # time limit exceed
    a = []
    # p = 1
    for i in range(0, len(nums)):
        p = 1
        for j in range(0, len(nums)):
            if j != i:
                p *= nums[j]
        print(p)
        a.append(p)
    print(a)


def productExceptSelf2(nums): # time limit exceed

    res = [1]*len(nums)
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix*=nums[i]

    postfix = 1
    for j in range(len(nums)-1,-1,-1):
        res[j] *= postfix
        postfix*=nums[j]
    return res



if __name__ == "__main__":
    productExceptSelf2([1, 2, 3, 4])
