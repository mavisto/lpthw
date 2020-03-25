from sys import argv

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("That's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


print("Or we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do maths inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("We can combine the two, variables and maths")
cheese_and_crackers(amount_of_cheese +  100, amount_of_crackers + 1000)

def more_c_and_c():
    arg1 = input("Number of cheeses: ")
    arg2 = input("Number of crackers: ")
    print(f"Cheeses = {arg1} and Crackers = {arg2}")
    cheese_and_crackers(arg1, arg2)

more_c_and_c()

def more_c_and_c_again():
    arg3 = argv[1]
    arg4 = argv[2]
    cheese_and_crackers(arg3, arg4)

more_c_and_c_again()
