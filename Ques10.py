# Q10. Write a python script to print all prime numbers with a range 
#       start(15)
#       end  (45)
for a in range (15,45):  
    if a>1:  
        for i in range(2,a):  
            if (a%i)==0:  
                break  
        else:  
            print(a,end=' ')