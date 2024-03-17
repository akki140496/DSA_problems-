# ques1. Find the length of the desired string
def string_length(str1):
     count = 0
     for char in  str1:
         count += 1
     return count

if __name__=="__main__":
    k = input("Enter the desired string: ")
    print(string_length(k))

