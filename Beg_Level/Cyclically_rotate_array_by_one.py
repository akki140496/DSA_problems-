# arr = [1,2,3,4,5]
# n = len(arr)
# print(arr[n-1])
# arr.insert(0,arr[n-1])
# print(arr)
# arr.pop()
# print(arr)

# User function Template for python3

def rotate(arr, n):
    arr.insert(0, arr[n - 1])
    arr.pop()
    return arr


# {
# Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())

    while (T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        rotate(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends