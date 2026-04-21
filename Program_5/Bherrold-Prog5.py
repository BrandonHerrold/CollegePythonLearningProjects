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
#   This file is Maintained on Github:
#   https://github.com/BrandonHerrold/CollegePythonLearningProjects/tree/main/Program_5
# Goal:
# As defined in my coursework requirements:
#   Be able to read the datable from a database and perform the following:
#       Display all Tickets
#       Add a ticket
#       Filter by Offender Sex (M/F)
#       Save and Exit
#==================================

import sqlite3

class Ticket:
    def __init__(self, tid, actual_speed, posted_speed, age, violator_sex):
        self._tid = tid
        self._actual_speed = actual_speed
        self._posted_speed = posted_speed
        self._age = age
        self._violator_sex = violator_sex

    def getMphOver(self):
        return self._actual_speed - self._posted_speed
    
    def displayRow(self):
        return "%-10d %-12d %-10d %-8d %-15s" % (
            self._tid,
            self._posted_speed,
            self.getMphOver(),
            self._age,
            self._violator_sex
        )

def introduction():

    print('''
        Welcome to the Speed Offender Database Search System.
          With this program you have the following options:
        
        1. Display all Tickets
        2. Add a Ticket
        3. Filter Tickets by Offender Sex (Male/Female)
        4. Save & Exit

        ''')

def displayAllTickets(cursor):
    cursor.execute("SELECT tid, actual_speed, posted_speed, age, violator_sex FROM tickets")
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("\nNo tickets found in database. Please add any new tickets, or check file.")
        return
    
    print("\n%-10s %-12s %-10s %-8s %-15s" %
          ("TicketID", "Posted MPH", "MPH Over", "Age", "Violator Sex"))
    print("==========================================================")

    for row in rows:
        ticket = Ticket(row[0], row[1], row[2], row[3], row[4],)
        print(ticket.displayRow())

    print()

def saveAndExit(connector):
                
        print("\nSaving to database. Please wait...")
        connector.commit()
        connector.close()
            
        input("\nDatabase saved. Press Enter to exit program.")

def databaseLoad():
   
    print("Attempting to reach database...")

    try:
        connector = sqlite3.connect("tickets5.db")
        cursor = connector.cursor()

        cursor.execute("SELECT COUNT(*) FROM tickets")
        count = cursor.fetchone()[0]

        print("Database connection established."
              "\nTotal records in tickets database: ", count)
        
        return connector, cursor
    
    except sqlite3.Error:
        print("Error: Database not reached, please check folder, and verify database is inside.")
        return None, None

def main():

    
    connector, cursor = databaseLoad()
    
    if connector is None or cursor is None:
        return

    introduction()

    while True:
        choice = input("\nPlease enter your choice, 1, 2, 3, or 4:  ")

        if choice == "1":
            displayAllTickets(cursor)
        
        elif choice == "2":
            '''addTicket(connector, cursor)'''
            print("Function unavailable at this time.")
        
        elif choice == "3":
            '''filterByOffenderSex(cursor)'''
            print("Function unavailable at this time.")

        elif choice == "4":
            saveAndExit(connector)
            break

        else:
            print("\nError: Invalid choice. Please enter 1, 2, 3 or 4.\n")


main()
