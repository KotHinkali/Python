a=int(input())
b=int(input())
c=int(input())
nums=sorted([a,b,c])
if nums[1]-nums[0]==nums[2]-nums[1]:
    print("А")
elif nums[1]/nums[0]==nums[2]/nums[1]:
    print("Г")
else:
    print("No")