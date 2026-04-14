# Brandon Herrold
# CIT 144
# Program 5 - Working with Sqlite3 and Python
# Date: 04/13/2026
# Last date updated: 04/13/2026
# About:
#   This program has been assigned to me in order to demonstrate my ability to setup a program that
#   is meant to interact with sqlite3, and use Python to essentially go through and display chosen option
#   back to the user. We will also allow the user to add more tickets to the database.
#
#
#

# 
#   This file is Maintained on Github:
#   
# Goal:
# As defined in my coursework requirements:
#   Be able to read the datable from a database and perform the following:
#       Display all Tickets
#       Add a ticket
#       Filter by Offender Sex (M/F)
#       Save and Exit
#==================================

import sqlite3


def databaseLoad():
   
    print("Attempting to reach database...")

    try:
        connector = sqlite3.connect("tickets5.db")

        cursor = connector.cursor()
        cursor.execute("SELECT COUNT(*) FROM tickets")
        count = cursor.fetchone()[0]

        print("Database connection established."
              "\nTotal records in tickets database: ", count)
        
    except:
        print("Error: Database not reached, please check folder, and verify database is inside.")
        return

    # Run welcome AFTER successful connection to sqlite3 db file
    welcome()

def welcome():

    print('''
        Welcome to the Speed Offender Database Search System.
          With this program you have the following options:
        
        1. Display all Tickets
        2. Add a Ticket
        3. Filter Tickets by Offender Sex (Male/Female)
        4. Save & Exit

        ''')
    return
    main()

def main():

    while True:
        print(welcome())
        choice = input("Please enter your choice, 1, 2, 3, or 4: ")


# def displayTicketsAll():  #Ticket Display Function for all Tickets

databaseLoad()

