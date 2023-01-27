# Q4. write a python script to print first 10 multiples of N in reverse order ?
x=int(input("Enter a Number you want Multiple :"))
for a in range(x*10,0,-x):
    print(a,end=' ')