#program to find given input is anagram
def are_Anagram(a,b):
    a=a.lower()
    b=b.lower()
    return sorted(a)==sorted(b)
input1="Race"
input2="ecaR"
if (are_Anagram(input1,input2)):
    print(f"{input1} and {input2} both are anagram")
else:
    print(f"{input1} and {input2} both are not anagram")