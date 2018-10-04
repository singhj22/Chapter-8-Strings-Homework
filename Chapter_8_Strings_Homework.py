'''
Created on Oct 3, 2018
@author: Jugat Singh
Period 5 Python Even Days
'''
firstName= input('Please enter your first name: ')
lastName= input('Please enter your last name: ')

firstInitial = firstName[0]
lastInitial = lastName[0]

print("\n\n")

print("Full Name: ", firstName, lastName, "\t", "Initials: ", firstInitial, lastInitial)

print("\n")

print("Length of first name: ", len(firstName), "\t", "Length of last name: ", len(lastName), "\t", "Length of full name: ", len(firstName+lastName))


