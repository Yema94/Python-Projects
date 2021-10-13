# BMI Calculator

def calculateBMI(height, weight):
    heightInMeters = height * 0.4536
    bmi = weight / (heightInMeters * heightInMeters)
    return bmi

print(calculateBMI(5.5, 73.8)) 