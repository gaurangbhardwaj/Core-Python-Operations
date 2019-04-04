name=input("Enter your Fullname : ")

Roll=input("Enter Roll number : ")

submarks=[]
i=0
while(i<5):
    print("\nEnter marks of subject ",i+1," : ")
    submarks.append(int(input()))
    i+=1
    
print("--------------------------Mark Sheet------------------------")
    
i=0
while(i<5):
    if(submarks[i]>=90):
        grade='O'
    elif(submarks[i]>=80 and submarks[i]<90):
        grade='A+'
    elif(submarks[i]>=70 and submarks[i]<80):
        grade='A'
    elif(submarks[i]>=60 and submarks[i]<70):
        grade='B'
    elif(submarks[i]>=50 and submarks[i]<60):
        grade='C'
    elif(submarks[i]>=40 and submarks[i]<50):
        grade='D'
    else:
        grade='F'
    print("Suject ",i+1," marks = ",submarks[i], " grade awarded = ",grade)
    i+=1
input("Press any key to exit")