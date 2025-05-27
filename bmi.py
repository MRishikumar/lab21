def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height ** 2)
    print("BMI = " + str(round(bmi , 2)))

    if bmi < 18.5:
        print("Underweight")
    elif bmi > 25:
        print("Overweight")
    else:
        print("Acceptable")

calculate_bmi(weight = 70, height = 1.80)

    