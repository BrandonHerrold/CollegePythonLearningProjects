#Name: Brandon Herrold
#CIT144 Programming Project 1
#
#Assignment Decisions and Temperature Conversion
#Date: 1/21/2026


#For Loop exit Error case
tempVal = None
tempChoice = None

#Prompt for temperature value

#Discovered a ValueError: Could not convert string to float - if the user input any letters and chose to press enter during the input. 
#Adding a for loop, with 3 attempts:

for attempts in range(2):
    tempInput = input("Please enter the temperature value (i.e. 35, or 22) to convert: ")

    if tempInput.isdigit():
        tempVal = float(tempInput)
        break
    else:
        print("Error: Please enter a numeric value.\n")


if tempVal == None:
    print("Too many invalid attempts have been made.\n")
    input("Press Enter to Exit, and then restart the program...")

    quit()
   


print()
#Prompt for conversion choice (C or F)
tempChoice = input("Do you wish to convert to Fahrenheit or Celsius?\nPlease Enter C or F: ")

#Using the Decision Tree to execute the conversions.

if tempChoice == "C" or tempChoice == "c":
    print()
    print("You chose to convert: ", tempVal, "degrees F to Celsius.")
    print()
    degF = tempVal

    degC = round((degF-32) / 1.8, 1)
    print("The result of this conversion is: ", tempVal, "degrees F =", degC, "degrees C")
    print()
    input("Please press Enter to close this program")

elif tempChoice == "F" or tempChoice == "f":
    print()
    print("You chose to convert: ", tempVal, "degrees C to Fahrenheit")
    print()
    degC = tempVal

    degF = round((1.8 * degC) + 32, 1)
    print("The result of this conversion is: ", tempVal, "degrees C =", degF, "degrees F")
    print()
    input("Please press Enter to close this program")

else:
    print()
    print("Error: Invalid input detected.")
    input("Press enter to close..")
