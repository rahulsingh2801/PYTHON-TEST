# class agecal:  # class must be in upper case
#     print("class concept")

#     def my_function(birthYear, currentYear):
#         ageYear = currentYear - birthYear
#         print("Your age is : ", ageYear)


# age = agecal() # object must be in lower  case
# birthYear = int(input("Enter birth Year"))
# currentYear = 2024
# # age.my_function(birthYear, currentYear)  
# agecal.my_function(birthYear,currentYear)  

#question 2nd

# def calculate_bmi(weight_kg, height_m):

#     try:
#         bmi = weight_kg / (height_m ** 2)
#         return bmi
#     except ZeroDivisionError:
#         return 

# def main():
#     try:
#         weight_kg = float(input("Enter your weight in kilograms: "))
#         height_m = float(input("Enter your height in meters: "))
#         bmi_result = calculate_bmi(weight_kg, height_m)
#         print(f"Your BMI is: {bmi_result:.2f}")
#     except ValueError:
#         print("Invalid input. Please enter numeric values for weight and height.")


#question 3rd


print("Currency Converter");
rsIntoDollar = int(input("Enter Amount in $ "));
rupeesAmount = (rsIntoDollar*84)   #Dollar to rupees
rupeesAmount = (rsIntoDollar/84)  #Dollar to rupees

print(rsIntoDollar ," $ Convert into Rupees " , rupeesAmount)
