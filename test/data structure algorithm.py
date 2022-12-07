# n=int(input())

# result = n*(n+1)/2

# print(result)


# for x in range(6):
#   if x == 3:
#    break
#   print(x)
# else:
#   print("Finally finished!")

# #If the loop breaks, the else block is not executed.

# i = 1
# while i < 6:
#     print(i)
#     i = i+1


# #------------------------------Linear search algorithm implement-----------------------------

# arr = [1,3,5,6,7,8,13,324,3434,6787]

# finding = int(input())

# for i in arr:
#     if finding == i:
#         print('Number is fund here...',)
# else:
#     print('Opps! number not')


# #-----------------------------------binary search algorithm implement-----------------------------



# # Python 3 program for recursive binary search.
# # Modifications needed for the older Python 2 are found in comments.
 
# # Returns index of x in arr if present, else -1
# def binary_search(arr, low, high, x):
 
#     # Check base case
#     if high >= low:
 
#         mid = (high + low) // 2
 
#         # If element is present at the middle itself
#         if arr[mid] == x:
#             return mid
 
#         # If element is smaller than mid, then it can only
#         # be present in left subarray
#         elif arr[mid] > x:
#             return binary_search(arr, low, mid - 1, x)
 
#         # Else the element can only be present in right subarray
#         else:
#             return binary_search(arr, mid + 1, high, x)
 
#     else:
#         # Element is not present in the array
#         return -1
 
# # Test array
# arr = [ 2, 3, 4, 10, 40 ]

# print('to see the last element', 4//2)
# x = 3
 
# # Function call
# result = binary_search(arr, 0, len(arr)-1, x)
 
# if result != -1:
#     print("Element is present at index", str(result))
# else:
#     print("Element is not present in array")


# def binary_search_nayem(arrey,low,high,searching_number):

#     if low <= high:

#         mid = (low + high) //2

#         # print(mid)

#         if arrey[mid] == searching_number:
#             print('Here is your desire number you looking for....',arrey[mid])

#         elif arrey[mid] > searching_number:
        
#             binary_search_nayem(arrey,0,mid-1,searching_number)
#         else:
 
#             binary_search_nayem(arrey,mid+1,high,searching_number)
#     else:
#         print('Ops! the number not found')
        
    

# arrey = [5,9,17,18,26,44,59,62,74,670,765]

# searching_number = int(input())

# binary_search_nayem(arrey,0,len(arrey)-1,searching_number)

# def binary_search(arr,less,greater,find):
#     if less <= greater:
#         mid = (less + greater)//2
#         if arr[mid] == find:
#             print(arr[mid])
#         elif arr[mid] > find:
#             binary_search(arr,0, mid-1,find)
#         else:
#             binary_search(arr,mid+1,greater,find)
#     else:
#         print('number not found')
# arr = [1,5,6,8,9,12,34,67,80,409]
# find = int(input())

# binary_search(arr,0,len(arr)-1,find)



# # Selection sort in Python
# # time complexity O(n*n)
# # sorting by finding min_index
# def selectionSort(array, size):
                                                                                                                                                                                                                          
#     for ind in range(size):
#         min_index = ind
 
#         for j in range(ind + 1, size):
#             # select the minimum element in every iteration
#             if array[j] < array[min_index]:
#                 min_index = j
#          # swapping the elements to sort the array
#         (array[ind], array[min_index]) = (array[min_index], array[ind])

#         print(array[ind])
 
# arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
# size = len(arr)
# selectionSort(arr, size)
# print('The array after sorting in Ascending Order by selection sort is:')
# print(arr)



# arr = [4,-5,76,3,-78,53]
# lenth = len(arr)
# for i in range(lenth):
#     j = i
#     for k in range(i+1,lenth): 
#         if arr[k] < arr[i]:
#             print(arr[k])
#             i = k
#     (arr[i], arr[j])=(arr[j],arr[i])

# print(arr)  


def binary_search(arr,less,greater,finding): 

    middle = (less+greater)// 2
    if less <= greater:
        if arr[middle] == finding:
            print(arr[middle])

        elif finding > arr[middle]:
            binary_search(arr,middle+1,greater,finding)
        else:
            binary_search(arr,less,middle-1,finding)
    else:
        print('number not found')
          
arr = [1,5,6,9,12,45,67,89]
finding = 60
less = 0
greater = len(arr)-1
binary_search(arr,less,greater,finding)




                                                                                                    
    



