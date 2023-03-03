weight = float(input("Enter Weight in Pounds: "))
f = int(input("Enter Your Height (feet): "))
i = int(input("Enter Your Height (inches): "))

f = f * 12
height = f + i
bmi = (703 * weight)/(height*height)


if bmi < 18.5:
    status = "You are Underweight"

elif bmi < 25:
    status = "You are is Normal"

elif bmi < 30:
    status = "You are Overweight"

else:
    status = "You are Obesity"

print("Your BMI is: ", bmi, "and", status)