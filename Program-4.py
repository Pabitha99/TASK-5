#to print the number of unique of characters from input
def UniqueChar(s):
    a=set(s)
    return len(a)
if __name__=="__main__":
    input_String="Guvi Private Limited"
    print(UniqueChar(input_String))
