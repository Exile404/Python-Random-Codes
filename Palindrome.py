def palindrome(s):
    n=len(s)
    for i in range(len(s)//2):
        if s[i]!=s[n-i-1]:
            return False
    return True

s=input()
c=palindrome(s)
if c==True:
    print("Palindrome")
else:
    print("Not palindrome")