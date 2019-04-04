def SumOfDigit(num):
    sum=0
    temp=0
    while(num>0):
        temp=num%10
        sum=sum+temp
        num=int(num/10)
    print("\nSum of digit = ",int(sum))
    
def Armstrong(num):
    sum=0
    arm=num
    temp=0
    while(num>0):
        temp=num%10
        sum=sum+(temp**3)
        num=int(num/10)
    if(arm==sum):
        print("\nIt's an armstrong number")
    else:
        print("\nNot an armstrong number")
        
def FourthDegree(num):
    fd=(num**4)+(3*(num**3))+(2*(num**2))+(5*num)+1
    print("\nFourth degree of number =",fd)



num=int(input("Enter Roll number : "))



SumOfDigit(num)
Armstrong(num)
FourthDegree(num)

        