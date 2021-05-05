#pyramid

#1. star pyramid
"""
def pattern(n):
    k=2*n-2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for j in range (0,i+1):
            print("* ", end="")
        print("\r")

pattern(5)
"""""

#2.inverted star pyramid
"""
def pattern(n):
    k=n-3
    for i in range(n-1,-1,-1):
        for j in range(k,0,-1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")

pattern(5)
"""


#3.left start pattern pyramid

"""
def pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
    for i in range (n,-1,-1):
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")

pattern(5)
"""

#4.right start pattern pyramid

def pattern(n):
    k=2*n-2
    for i in range(0,n-1):
        for j in range(0,k):
            print(end=" ")
        k=k-2
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
    k=-1
    for i in range (n-1,-1,-1):
        for j in range(k,-1,-1):
            print(end=" ")
        k=k+2
        for j in range(0,i+1):
            print("* ", end="")
        print("\r")

pattern(10)



