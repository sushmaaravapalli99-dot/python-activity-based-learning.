print("Railway Fare Calculator")

n = int(input("Enter number of passengers: "))
total = 0

for i in range(n):
    print("\nPassenger", i + 1)

    age = int(input("Enter age: "))
    distance = int(input("Enter distance in km: "))

    print("1. Sleeper")
    print("2. AC")
    choice = int(input("Choose class: "))

    # Distance fare
    if distance <= 100:
        fare = distance * 2
    elif distance <= 500:
        fare = distance * 3
    else:
        fare = distance * 4

    # Class fare
    if choice == 2:
        fare = fare * 2

    # Age discount
    if age < 5:
        fare = 0
    elif age >= 60:
        fare = fare * 0.8

    # Reservation fee
    fare = fare + 50

    print("Passenger fare: Rs.", fare)
    total = total + fare

print("Total fare: Rs.", total)

cancel = input("Cancel tickets? (yes/no): ")

if cancel == "yes":
    print("Cancellation penalty: Rs.", total * 0.25)
    print("Refund: Rs.", total * 0.75)
else:
    print("Reservation confirmed!")

