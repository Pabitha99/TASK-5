def lcs(X,Y,i,j):
    #to check if size of both strings equal to zero
    if(i==0 or j==0):
        return 0
    if(X[i-1]==Y[j-1]):
        return 1+lcs(X,Y,i-1,j-1)
    else:
        #to get the maximum number of characters
        return max(lcs(X,Y,i-1,j),lcs(X,Y,i,j-1))

A1=input()
#geting string1 from the user input 
A2=input()
#geting string2 from the user input
s1=len(A1)
s2=len(A2)
print(lcs(A1,A2,s1,s2))
 