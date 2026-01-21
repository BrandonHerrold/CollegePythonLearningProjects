#Name: Brandon Herrold

# Assignment Decisions and Temperature Conversion

#Prompt for temperature value

tempVal = float(input("Please enter the temperature value to convert: "))
print()
#Prompt for conversion choice (C or F)
tempChoice = input("Do you wish to convert to Fahrenheit or Celsius?\nPlease Enter C or F: ")

#Using the Decision Tree to execute the conversions.

if tempChoice == "C":
    print()
    print("You chose to convert: ", tempVal, "from Fahrenheit to Celsius.")
    print()
    degF = tempVal

    degC = round((degF-32) / 1.8, 1)
    print("The result of this conversion is: ",tempVal,"F to ",degC,"C")

elif tempChoice == "F":
    print()
    print("You chose to convert: ",tempVal, " from Celsius to Fahrenheit")
    print()
    degC = tempVal

    degF = round((1.8 * degC) + 32, 1)
    print("The result of this conversion is: ", tempVal, "C to", degF, "F")

else:

    print("Error: Please enter either F or C.")
