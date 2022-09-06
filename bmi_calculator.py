#BMI calculator
height = float(input("Please enter your height(cm)\n"))
weight = float(input("Please enter your weight(kg)\n"))

height /= 100
bmi = weight / height**2
bmi = round(bmi, 1)
print(f"Your BMI is: {bmi}")

height = float(input("Please enter your height(cm)\n"))
weight = float(input("Please enter your weight(kg)\n"))

height /= 100
bmi = weight / height**2
bmi = round(bmi, 1)
print(f"Your BMI is: {bmi}")

if bmi < 18.5:
    print(f"Your BMI is: {bmi} (Underweight)")
elif bmi < 24:
    print(f"Your BMI is: {bmi} (Healthy)")
elif bmi < 27:
    print(f"Your BMI is: {bmi} (Overweight)")
elif bmi < 30:
    print(f"Your BMI is: {bmi} (Slightly Obese)")
elif bmi < 35:
    print(f"Your BMI is: {bmi} (Obese)")
else:
    print(f"Your BMI is: {bmi} (Over Obese)")
