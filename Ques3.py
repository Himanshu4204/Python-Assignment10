# Q3. write a python script to print first M multiples of N ?
a=int(input("Enter a Number you want Multiple :"))
b=int(input("Enter how many multiples you want :"))
for x in range(a,a*b+a,a):
    print(x,end=' ')
