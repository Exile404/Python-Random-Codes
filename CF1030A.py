n=int(input())
l=list(map(int,input().split()))
# check=True
# for i in l:
#     if i==1:
#         print("HARD")
#         check=False
#         break
# if check:
#     print("EASY")
if 1 in l:
    print("HARD")
else:
    print("EASY")
