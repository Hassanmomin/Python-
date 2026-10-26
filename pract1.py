table = {
("A","Dirty") : "suck",
("A","Clean") : "Move Right",
("B","Dirty") : "suck",
("B","Clean") : "Move Left",
    }

location = input("Enter Location(A/B):")
status= input("Enter Status(Dirty/Clean):")
action = table.get((location,status),"Invalid Input")
print("\nPersept:",(location,status))
print("Action:",action)
