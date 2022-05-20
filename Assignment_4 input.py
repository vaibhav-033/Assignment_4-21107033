#Q1

marks=float(input("Enter your marks here: "))
if marks<25:
    print("Your Grade is : F")
elif 25<=marks<45:
    print("Your grade is : E")
elif 45<=marks<50:
    print("Your grade is : D")
elif 50<=marks<60:
    print("Your grade is : C")
elif 60<=marks<80:
    print("Your grade is : B")
elif 80<=marks<100:
    print("Your grade is : A")
else:
    print("Invalid input")


#Q2

year=int(input("Enter the year here: "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(str(year)+" is a leap year")
        else:
            print(str(year)+ " is not a leap year")
    else:
        print(str(year)+" is a leap year")
else:
    print(str(year)+" is not a leap year")


#Q3

from random  import randint
for i in range(1,11):
    n1=randint(1,10)
    n2=randint(1,10)
    guess=int(input("Question " + str(i) + ": " + str(n1)+ "x" + str(n2)+ " = "))
    answer=n1*n2
    if guess==answer:
        print("Right!")
    else:
        print("Wrong. The correct answer is:", answer)


#Q4

for y in range(200):
    if y%5==2:
        if y%6==3:
            if y%7==2:
                print("There are " + str(y) + " candies in total.")