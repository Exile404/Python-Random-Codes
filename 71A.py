n=int(input())
for i in range(n):
    s=input()
    sz=len(s)
    if sz<=10:
        print(s)
    else:
        print(f'{s[0]}{sz-2}{s[sz-1]}')