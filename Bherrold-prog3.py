#Name: Brandon Herrold
#CIT144 Programming Project 3
#
#Emporium Sales Program
#Date: 03/16/2026
#About: This program is mean to demonstrate my ability to extract information
#       from an existing data file (text), and format it, along with parsing, and setting up the calculations
#       for the total of each purchase made.


# Helper functions
def calculate_total(price, quantity):
    
    # Perform the Calculation
    order_total = price * quantity

    # Return the result to caller
    return order_total

def main():
    
    grand_total = 0

    # Extracting Data file
    sales_file = open("makewaves.txt", "r")

    #Top line print
    print("%-10s %-25s %5s %5s %10s" % ("Customer", "Item", "Price", "Qty", "Total"))
    print("===========================================================")


    # loop through each line
    for line in sales_file:

        # Remove newline char, split into pieces, extract fiels, then convert numeric values.
        line = line.strip()
        data = line.split(",")

        customer = data[0]
        item = data[1]

        price = float(data[2])
        quantity = int(data[3])

        # Call the order total function
        order_total = calculate_total(price, quantity)

        # Add to running total, a.k.a grand_total
        grand_total = order_total + grand_total

        # Print the rows in formatted style
        print("%-10s %-25s %5.2f %5d %10.2f" % (customer, item, price, quantity, order_total))
            

    # Close the file when complete
    sales_file.close()

    # Print final total
    print("===========================================================")
    print("\nTotal sales for the day: $%0.2f" % grand_total)

# Start the program
main()
input()