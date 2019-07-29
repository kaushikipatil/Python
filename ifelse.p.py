


number=int(input("Enter your marks"))

print(number)

if (number>90 and number<100):
    grade = 'A'
elif (number>80 and number<89):
    grade = 'B'
else:
    grade='Fail'

print("The grade is ", grade)