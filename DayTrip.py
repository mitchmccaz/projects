import random
from tkinter import Y
my_destinations = ("New Mexico", "Arizona", "Florida", "Mississippi")
place = random.choice(my_destinations)

my_transportation = ("Car", "Buss", "Plane", "Bike")
transportation = random.choice(my_transportation)

my_restaurants = ("Texas Longhorn", "Joe's Crab Shack", "Wendys", "El Paso")
food = random.choice(my_restaurants)

my_entertainment = ("Swimming", "Karaoke", "Movies", "Comedy Club" )
fun = random.choice(my_entertainment)

day_trip = (f"Destination: {place} Transportation: {transportation} Restaurant: {food} Entertainment: {fun}")
print(day_trip)

confirm_choice = input("Are you Satisfied y/n?")
if confirm_choice == "y":
    print("Enjoy your Day trip!!")
else:

 def new_destination(confirm_choice):
    while confirm_choice != "y":
        place = random.choice(my_destinations)
        confirm_choice = input(f"{place}? :")
    else:
        print(f"You have selected {place}")
 new_destination = (confirm_choice)

 def new_restaurant(confirm_choice):  
   while confirm_choice != "y":
     food = random.choice(my_restaurants)
     confirm_choice = input(f"{food}? :")
   else:
     print(f"You have selected {food}.")
 new_restaurant(confirm_choice)

 def new_trans(confirm_choice):  
   while confirm_choice != "y":
     transportation = random.choice(my_transportation)
     confirm_choice = input(f"{transportation}? :")
   else:
     print(f"You have selected {transportation}")
 new_trans(confirm_choice)

 def new_entertainment(confirm_choice):  
  while confirm_choice != "y":
     fun = random.choice(my_entertainment)
     confirm_choice = input(f"{fun}?")
  else:
     print(f"You have selected {fun} ")
 new_entertainment(confirm_choice)
            