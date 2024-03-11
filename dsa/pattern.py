# * * *
# * * *
# * * *

# n=10
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
    
#     print()

# --------------------------------------------------------

# * 
# * * 
# * * *


# n=10
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")

#     print()

# --------------------------------------------------------
# 1
# 1 2 
# 1 2 3

# n=10
# for i in range(n):
#     for j in range(i+1):
#         print(j+1,end="")

#     print()

# --------------------------------------------------------
# 1
# 2 2 
# 3 3 3

# n=10

# for i in range(n):
#     for j in range(i+1):
#         print(i+1,end="")

#     print()

# --------------------------------------------------------
# * * *
# * *
# *

# n=10
# for i in range(n):
#     for j in range(n-i):
#         print('*',end="")
   
#     print()

# --------------------------------------------------------
# 1 2 3
# 1 2
# 1
    
# n=10
# for i in range(n):
#     for j in range(n-i):
#         print(j+1,end="")
#     print()    

# --------------------------------------------------------
#   *
#  ***
# *****
    
# n=10
# for i in range(n):
#     for j in range(n-i-1):
#         print('|',end="")

#     for j in range(2*i+1):
#         print('*',end="")

#     print()  
 
# --------------------------------------------------------
# *****
#  ***
#   *

# n=10
# for i in range(n):
    
#     for j in range(i):
#         print('|',end="")

#     for j in range(2*n-2*i-1):
#         print('*',end="")

#     print()  

# --------------------------------------------------------
#   *  
#  ***
# ***** 
# *****  
#  ***
#   * 
    
# n=10

# for i in range(n):
#     for j in range(n-i-1):
#         print('|',end="")

#     for j in range(2*i+1):
#         print('*',end="")

#     # for j in range(2*i+1):
#     #     print('*',end="")

#     print()

# for i in range(n):
    
#     for j in range(i):
#         print('|',end="")

#     for j in range(2*n-2*i-1):
#         print('*',end="")

#     print()  
    
# --------------------------------------------------------
#   *  
#   **
#   ***  
#   **
#   *

# n=10
# for i in range(n):
#     for j in range(i+1):
#         print('*',end="")
        
#     print()

# for i in range(n):
#     for j in range(n-i-1):
#         print('*',end="")
        
#     print()

# --------------------------------------------------------
# 1
# 01
# 101
# n=3

# for i in range(n):
#     for j in range(i+1):
#         if((i+j)%2==0):
#           print('1',end="")
#         else:
#            print('0',end="")
        
#     print()

# --------------------------------------------------------
# 1    1
# 12  21
# 123321

# n=6

# for i in range(n):
#     for j in range(i+1):
#         print(j+1,end="")

#     for j in range((n-i-1)*2):
#         print("|",end="")

#     for j in range(i+1,0,-1):
#         print(j,end="")


#     print()
    
# --------------------------------------------------------
# 1
# 2 3
# 4 5 6

# n=5
# k=1
# for i in range(n):
#     for j in range(i+1):
#         print(k,end=" ")
#         k +=1
#     print()


# --------------------------------------------------------
# A
# A B
# A B C

def numToChr(num):
    return chr(num+65)
# n=3

# for i in range(n):
#     for j in range(i+1):
#         print(numToChr(j),end=" ")
#     print()


# --------------------------------------------------------
# A B C
# A B
# A

# n=3
# for i in range(n):
#     for j in range(n-i):
#         print(numToChr(j),end=" ")
#     print()

# --------------------------------------------------------
# A
# B B
# C C C

# n=3
# for i in range(n):
#     for j in range(i+1):
#         print(numToChr(i),end=" ")
#     print()

# --------------------------------------------------------
#   A  
#  ABA 
# ABCBA

# n=3

# for i in range(n):
#     for j in range(n-1-i):
#         print(" ",end="")

#     for j in range(i):
#         print(numToChr(j),end="")

#     for j in range(i,-1,-1):
#         print(numToChr(j),end="")


#     print()
    
# --------------------------------------------------------
# C
# B C
# A B C