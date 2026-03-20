#Name: Brandon Herrold
#CIT144 Programming Project 2
#
#Exam Score Averaging Project
#Date: 2/21/2026
#About:
#   This program allows users to enter a series of exam scores. There is no limit to the number of
#   scores that can be entered. The scores can be integers or floats. Once the scores hav all been entered
#   the user needs only to enter a sentinel value in order to exit, and then it gives the average of the scores.


print("""Welcome to the Grade Average calculation program.
      You may enter the scores in either format below:
      Such as 19, 22, 30 or even in the form 55.5, 75.5, 99.5
      
      Once you are finished entering the scores, enter 9999.
      After entering 9999, the average of all the scores entered will be calculated.
      """)


total = 0.0         # Accumulator
count = 0           # Number of valid scores
sentinel = 9999     # Numeric sentinel value
max_score = 100     # Maximum valid score
min_score = 0       # Minimum valid score

score = float(input("Enter the exam score, or 9999 to quit: "))

while score != sentinel:

    if score < min_score or score > max_score:
        print("That score is not within range. Please re-enter a valid score.")
    else:
        total = total + score
        count = count + 1
    
    score = float(input("Enter the exam score, or 9999 to quit: "))

if count > 0:
    average = total / count
    print(f"\nYou have entered {count} scores, and the average is: {average:.1f}")
else:
    print("\nNo valid scores were entered.")

print("\n\n\nThank you for using the Grade Average calculation program.")
input("Press any key to exit the program, and have a great day!")