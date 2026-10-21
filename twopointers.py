A = [1, 2, 3, 4, 6, 7]
B = [2, 3, 3, 4, 9, 11]

C = []

jj, kk = 0, 0

# Moving the smaller of the two outwards. 
# Becuase Anything before this would have been captured already.

while jj < len(A) and kk < len(B):
    if A[jj] == B[kk]:
        C.append(A[jj])
        kk += 1
    elif A[jj] < B[kk]: 
        jj += 1
    else: 
        kk += 1


print(C)


# What if there are repetitions. 




