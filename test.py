# Python3 program to find maximum
# in arr[] of size n

# python function to find maximum
# in arr[] of size n
def largest(arr, n):
    # Initialize maximum element
    max = arr[0]

    # Traverse array elements from second
    # and compare every element with
    # current max
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max

def smallest(arr, n):
    min = arr[0]

    for i in range(1, n):
        if arr[i] < min:
            min = arr[i]
    return min


def printDistinct(arr, n):
    newArray = []
    # Pick all elements one by one
    for i in range(0, n):

        # Check if the picked element
        # is already printed
        d = 0
        for j in range(0, i):
            if (arr[i] == arr[j]):
                d = 1
                break

        # If not printed earlier,
        # then print it
        if (d == 0):
            # newArray = arr[i]
            # print(arr[i])
    return newArray

# Driver program to test above function
arr = [6, 10, 5, 4, 9, 120, 4, 6, 10]
n = len(arr)


# This code is contributed by Sam007.
# Driver Code
arr = [1, 2, 3, 6, 4, 3, 1]
n = len(arr)
Ans = largest(arr, n)
res = smallest(arr,n)
print ("Largest in given array is", Ans , res)
# printDistinct(arr, n)
newRest = printDistinct(arr,n)
print(newRest)


