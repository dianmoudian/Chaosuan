def max_subarray_sum(arr):
    n = len(arr)
    if n == 0:
        return 0
    dp = [0] * n
    dp[0] = arr[0]
    max_sum = dp[0]
    for i in range(1,n):
        dp[i] = max(dp[i - 1]+arr[i],arr[i])
        max_sum = max(max_sum,dp[i])
    return max_sum

arr = [-20,11,-4,13,-5,-2]

print("最大子段和：",max_subarray_sum(arr))