#takes the string input
String="Guvi Geeks Network Private Limited"
newString=String
vowels=('a','e','i','o','u','A','E','I','O','U')
#returns the new string with all the vowels removed
for i in String:
    for j in vowels:
        newString=newString.replace(j,"")
print(newString)
