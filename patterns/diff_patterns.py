def pattern_one(n):
    for i in range(n):
        for j in range(n):
            print("*",end=" ")
        print()
    print()



pattern_one(6)

def patter_two(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end=" ")
        print()
    print()
patter_two(6)

def patter_three(n):
    for i in range(n):
        for j in range(n-i):
            print("*",end=" ")
        print()
    print()


patter_three(6)

def pattern_four(n):
    for i in range(n):
        for j in range(i+1):
            print(str(j+1),end=" ")
        print()
    print()
pattern_four(6)

def pattern_five(n):
    for i in range(2*n):
        ind = i if i + 1 <= n else (((2*n)-i)-2)
        for j in range(ind+1):
            print("*",end=" ")
        print()
    print()
pattern_five(5)

def pattern_six(n):
    for i in range(n):
        for l in range(n-(i+1)):
            print(" ",end=" ")
        for j in range(i+1):
            print("*",end=" ")
        print()
    print()
pattern_six(5)



def pattern_eight(n):
    for i in range(n):
        for l in range(n-(i+1)):
            print(" ",end=" ")
        for j in range(i+i+1):
            print("*",end=" ")
        print()
    print()
pattern_eight(5)

def pattern_nine(n):
    for i in range(n):
        for l in range(i):
            print(" ",end=" ")
        i += 1
        for j in range((n-i)+(n-i)+1):
            print("*",end=" ")
        print()
    print()
pattern_nine(5)

def pattern_ten(n):
    for i in range(n):
        for l in range(n-(i+1)):
            print(" ",end="")
        for j in range(i+1):
            print("*",end=" ")
        print()
    print()
pattern_ten(5)

def pattern_11(n):
    for i in range(n):
        for l in range(i):
            print(" ",end="")
        for j in range(n-i):
            print("*",end=" ")
        print()
    print()
pattern_11(5)

def pattern_12(n):
    for i in range(2*n):
        space = i if i <= n else i-1
        ind = n-i if i <=n else i-n
        for l in range(space):
            print(" ",end="")
        for j in range(ind):
            print("*",end=" ")
        print()
    print()
pattern_12(5)