word="Helooooooo World!!!!"
#print(word)
frq={}
for char in word:
    if char in frq:
        frq[char]+=1
        #counting each character
    else:
        frq[char]=1
max_key=max(frq,key=frq.get)
#to get maximum repeated character
print(f"the {max_key} has highest frequency of {frq[max_key]}")



