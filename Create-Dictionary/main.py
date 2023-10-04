# Sachin Karki
# Purpose: Assignment 05, Creating Dictionary
import os

# Using pp print libary to print the output nice and formatted
import pprint

os.system('clear')
# Creating dictionary for 1st tab and assigning keys and values to it
employee = {}
employee[1000] = {
    "first_name": "Bilbo",
    "last_name": "Baggins",
    "username": "barrel-rider"
}
employee[1001] = {
    "first_name": "Frodo",
    "last_name": "Baggins",
    "username": "nine-fingers"
}
employee[1002] = {
    "first_name": "Samwise",
    "last_name": "Gamgee",
    "username": "gardener"
}
employee[1003] = {
    "first_name": "Peregrin",
    "last_name": "Took",
    "username": "pippin"
}
employee[1004] = {
    "first_name": "Meriadoc",
    "last_name": "Brandybuck",
    "username": "merry"
}
# Creating dictionary for 2nd tab and assigning key and values to it
position = {}
position["C101"] = "Adventurer"
position["RB01"] = "Ring Bearer"
position["L777"] = "Luck Wearer"
position["S321"] = "Sojourner"
position["G001"] = "Gardener"
position["CR99"] = "Comic Relief"
position["K000"] = "Knight"

# Adding position information to individual employee
employee[1000]["position"] = ["C101", "RB01", "L777"]
employee[1001]["position"] = ["RB01", "S321"]
employee[1002]["position"] = ["G001", "S321", "RB01"]
employee[1003]["position"] = ["S321", "CR99", "K000"]
employee[1004]["position"] = ["S321", "K000"]

# Utlizing the pretty print libraby
pp = pprint.PrettyPrinter(indent=4)
# Prints employee dictionary nice and formatted
pp.pprint(employee)
print()
# Prompting user input to continue to next dictionary
input('Hit [ENTER] to Continue:')
print()
# Prints position dictionary nice and formatted
pp.pprint(position)
print()
