
def calculate_bmi(weight_kg, height_m):

    try:
        bmi = weight_kg / (height_m ** 2)
        return bmi
    except ZeroDivisionError:
        return 

def main():
    try:
        weight_kg = float(input("Enter your weight in kilograms: "))
        height_m = float(input("Enter your height in meters: "))
        bmi_result = calculate_bmi(weight_kg, height_m)
        print(f"Your BMI is: {bmi_result:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")

