
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TKAgg")
def linearsearch(thevalues,target):
    n=len(thevalues)
    for i in range(n):
        if thevalues[i]==target:
            return True
    return False
thevalues=[10,50,60,70,80,90,20]
target=20
if linearsearch(thevalues,target):
    print("the target value found in list")
else:
    print("the target value not found")
x=list(range(1,10000))
plt.plot(x,[y for y in x])
plt.title("linear search time complexity us o(n)")
plt.xlabel("input")
plt.ylable("time")



import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TKAgg")
def linearsearch(thevalues,target):
    n=len(thevalues)
    for i in range(n):
        if thevalues[i]==target:
            return True
    return False
thevalues=[10,50,60,70,80,90,20]
target=20
if linearsearch(thevalues,target):
    print("the target value found in list")
else:
    print("the target value not found")
x=list(range(1,10000))
plt.plot(x,[y for y in x])
plt.title("linear search time complexity us o(n)")
plt.xlabel("input")
plt.ylable("time")



        
