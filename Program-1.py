#to calculate the total number of vowels and count of each individual value
a="Guvi Geeks Private Limited"
count1a=0
count1A=0
count2e=0
count2E=0
count3i=0
count3I=0
count4o=0
count4O=0
count5u=0
count5U=0
Total=0
for i in a:
    if(i=='a'):
        count1a=count1a+1
    if(i=='A'):
        count1A=count1A+1
    if(i=='e'):
        count2e=count2e+1
    if(i=='E'):
        count2E=count2E+1
    if(i=='i'):
        count3i=count3i+1
    if(i=='I'):
        count3I=count3I+1
    if(i=='o'):
        count4o=count4o+1
    if(i=='O'):
        count4O=count4O+1
    if(i=='u'):
        count5u=count5u+1
    if(i=='U'):
        count5U=count5U+1
#to calculate the individual vowels count
print(" vowel a=",count1a)
print("Vowel A=",count1A)
print("Vowel e=",count2e)
print("Vowel E=",count2E)
print("Vowel i=",count3i)
print("Vowel I=",count3I)
print("Vowel o=",count4o)
print("Vowel O=",count4O)
print("Vowel u=",count5u)
print("Vowel U=",count5U)
#to calculate the total number of vowels
sum=count1a+count1A+count2e+count2E+count3i+count3I+count4o+count4O+count5u+count5U
print("Total Vowels count=", sum)  
    
