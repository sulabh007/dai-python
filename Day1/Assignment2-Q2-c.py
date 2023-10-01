
#########################Q2-b##########################
##num=int(input("Enter Number : "))
##if num%2==0:
##    print("number should be odd")
##else:
##    cnt=num//2
##    for i in range(1,num+1,2):
##        print(" "*cnt,"*"*i,sep="")
##        cnt=cnt-1
##    cnt=1
##    for i in range(num-2,0,-2):
##        print(" "*cnt,"*"*i,sep="")
##        cnt=cnt+1
##


#########################Q2-c##########################
##for i in range(7,0,-2):
##    for j in range((7-i)//2):
##         print(" ",end="")
##    for j in range(i) :
##        if j%2==0:
##           print("1",end="")
##        else:
##            print("0",end="")
##    print()

#########################Q2-d##########################

##for i in range(1,6):
##    for j in range(1,i+1):
##        print(f"{j} ",end="")
##    print()
#########################Q3##########################
##print("Enter Two Numbers")
##num1=int(input("Enter 1st number :"))
##num2=int(input("Enter 2nd number :"))
##
##x=1
##while num1!=0 and num2!=0:
##    if num1>num2:
##        x=num1%num2
##        num1=x
##        print(x)
##    elif num1<num2:
##        x=num2%num1
##        num2=x
##        print(x)
##    if num1==0:
##        x=num2
##    elif num2==0:
##        x=num1
##print(x)
#########################Q4##########################
##num=0
##choice=0
##i=0
##mul=0
##while choice!="q":
##    num=int(input("Enter number :"))
##    choice=str(input("Press q to Quit to countinue press any other key"))
##    num=num+num
##    mul=num
##    mul=num*mul
##    i=i+1
##avg=num/i    
##print(f"average is {avg} and product is {mul}")

#################################Q5############################
##ld=0
##add=0
##num=int(input("Enter a Number :"))
##while num!=0:
##    ld=num%10
##    num=num//10
##    add=add+ld
##print("Sum of digits is :",add)

#################################Q6############################

##num=int(input("Enter Number :"))
##for i in range(1,num):
##    cube=i*i*i
##    print(f"Cube of {i} :",cube)

#################################Q7############################

##print("Enter 20  Numbers :")
##s=0
##for i  in range(1,21):
##    num=int(input(f"Enter Number {i} : "))
##    if (num%2)==0:
##        s=s+num
##print(f"Total sum is : {s}")

#################################Q8############################
##num=int(input("Enter Number of terms to be generated : "))
##j=9
##s=0
##for i in range(num):
##    k=str(j)+(str(j)*i)
##    s=s+int(k)
##    print(k,end="")
##    if i<num-1:
##     print("+",end="")
##    else:
##        print("=",end="")
##print(s)

#################################Q9############################
##import math
##x=int(input("Enter of x : "))
##it=int(input("Enter Number of terms : "))
##s=1+x
##for i in range(2,it):
##    s=s+(x**i)/math.factorial(i)
##print("The sum is :",s)

#################################Q10############################


##x=2 #int(input("Enter of x : "))
##it=5 #int(input("Enter Number of terms : "))
##s=x
##
##for i in range(3,11,2):
##    #print(i)
##    j=i
##    if j%4==1:
##        s=s+(x**i)
##        print("Values :",s)
##        #print(i)
##    else:
##        s=s-(x**i)
##        print("Values :",s)
##s=x-s
##print("The sum is :",s)


x=int(input("Enter of x : "))
it=int(input("Enter Number of terms : "))
s=0
for i in range(0,it):
    s=s+((-1)**i)*x**(2*i+1)

print(s)


















    
