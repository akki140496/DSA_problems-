
# min_a = a[0]
# max_a = a[0]

# for i in range(0,n+1):
#     if (a[i]<a[i+1]):
#         max_a = a[i + 1]
#         min_a = a[i]
# print(max_a)
# print(min_a)
def getMinMax( a, n):
    min, max = a[1],0
    for i in range(0,n):
        if min < a[i]:
            if max < a[i]:
                max = a[i]
        else:
            min = a[i]
    return min, max

if __name__=="__main__":
    a = [1, 2, 3, 767, 33, 2, 0]
    n = len(a)
    print(getMinMax(a,n))
