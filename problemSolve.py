
# # **********************hakerrank.com python "Python If-Else"**************************

# n = input("Enter a number = ")
# n = int(n)

# if (n % 2) != 0:
#     print("Weird")

# elif n == 2 or n == 4:
#     print("Not Weird")

# elif n == 6 or n == 8 or n==10 or n==12 or n==14 or n==16 or n==18 or n==20:
#     print("Weird")

# elif n > 20:
#     print(" Not Weird")
    





# # **********************hakerrank.com python "Loops"**************************

# n = int(input())

# for i in range(0,n,1):
#     print(i*i)




# # **********************hakerrank.com python "function"**************************


# def is_leap(year):

#     if (year % 400 == 0) and (year % 100 == 0):
#         leap = True


#     elif (year % 4 ==0) and (year % 100 != 0):
#         leap = True

#     else:
#         leap = False

        
    
#     return leap

# year = int(input())
# print(is_leap(year))


# n = int(input())

# for i in range(n):
#     print(i,)

# # **********************hakerrank.com python "print function"**************************


# n = int(input())
# for i in range(1,n+1):
#     print(i, end = '')




list1 = [ 20, 20, 20, -20,-20]
 
mx = max(list1[0], list1[1])

secondmax = min(list1[0], list1[1])
n = len(list1)
for i in range(2,n):
    if list1[i] > mx:
        secondmax = mx
        mx = list1[i]
    elif list1[i] > secondmax and \
        mx != list1[i]:
        secondmax = list1[i]
    elif mx == secondmax and \
        secondmax != list1[i]:
          secondmax = list1[i]
 
print("Second highest number is : ",\
      str(secondmax))


# List of numbers
list1 = [57,-57,-57]
 
# Removing duplicates from the list
list2 = list(set(list1))
 
# Sorting the  list
list2.sort()
 
# Printing the second last element
print("Second largest element is:", list2[-2])