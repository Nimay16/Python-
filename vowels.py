s=str(input("Enter string:"))
count=0
vowels=set("aeiou")
for letter in s:
    if letter in vowels:
        count+=1
print(count)