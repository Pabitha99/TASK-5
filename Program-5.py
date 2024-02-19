#to check whether the input is palindrome
s=input()
#takes the input from the user
reverse_s=s[::-1]
#reversing the user input
if s==reverse_s:
    print("True")
else:
    print("False")

