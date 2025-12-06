word=input("Enter a letter: ")
x=['a','e','i','o','u']
i=0
for i in word :
    if i in x:
        print("It's a vowel")
        break
else:
    print("It's not a vowel")